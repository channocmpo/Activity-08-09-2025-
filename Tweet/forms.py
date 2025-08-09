from django import forms
from .models import Tweet

Banned_Words = ["Shit", "Fuck", "Bobo"]

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def clean_content(self):
        content = self.cleaned_data.get('content', "")
        for word in Banned_Words:
            if word.lower() in content.lower():
                raise forms.ValidationError("Your Tweet can't contain this word")

        return content

