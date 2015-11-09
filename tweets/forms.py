from django import forms

class TweetForm(forms.Form):
    #text = forms.CharField(widget = forms.Textarea(attrs = {
        #'rows':1, "columns":180,
        #}),
        #max_length = 180)
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 85}), max_length=160)
    country = forms.CharField(widget = forms.HiddenInput())

class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'size':32, 'class':'form-control'}),
            label='Enter a keyword to search for')

