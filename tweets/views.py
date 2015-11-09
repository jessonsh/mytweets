from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.templates import Context

from user_profile.models import User
from tweets.models import Tweet, HashTag
from .forms import TweetForm, SearchForm

# Create your views here.
def index(request):
    if request.method=='GET':
        return HttpResponse('I am called from a get request')
    elif request.method=='POST':
        return HttpResponse('I am called from a post request')

class Profile(View):
    def get(self, request, username):
        param = {}
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user = user)
        form = TweetForm()
        param['user'] = user
        param['tweets'] = tweets
        param['form'] = form
        return render(request, 'profile.html', param)

class ProfilePost(View):
    def post(self, request, username):
        form = TweetForm(self.request.POST)
        form.full_clean()
        if form.is_valid:
            user = User.objects.get(username = username)
            if user is not None:
                tweet = Tweet(
                        text = form.cleaned_data['text'],
                        country = 'China',
                        user = user,
                        )
                tweet.save()
                texts = form.cleaned_data['text'].split(' ')
                for text in texts:
                    if text.startswith('#'):
                        hashtag, created = HashTag.objects.get_or_create(name = text[1:])
                        hashtag.tweet.add(tweet)
            return HttpResponseRedirect('/user/' + username)

class HashTagCloud(View):
    def get(self, request, hashtag):
        hashtag = HashTag.objects.get(name=hashtag)
        param = {}
        if hashtag is not None:
            param['tweets'] = hashtag.tweet.all()
        return render(request, 'hashtag.html', param)

class Search(View):
    def get(self, request):
        search = SearchForm()
        params = {}
        params['search'] = search
        return render(request, 'search.html', params)
    def post(self, request, query):
        search = SearchForm(self.request.POST)
        search.full_clean()
        if search.is_valid:
            query = search.cleaned_data['query']
            tweets = Tweet.objects.filter(text__icontains=query)
            context = Context({'query':query, 'tweets':tweets})
            return_str = render_to_string('partials/_tweets_search.html')
            return HttpResponse(json.dumps(return_str))
        else:
            HttpResponseRedirect('/search')
