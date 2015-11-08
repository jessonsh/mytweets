from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from user_profile.models import User
from tweets.models import Tweet
from .forms import TweetForm

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

class PostTweet(View):
    def post(self, request, username):
        form = TweetForm(self.request.POST)
        if form.is_valid():

        
