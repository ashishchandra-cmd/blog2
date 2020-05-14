from django import forms

class Emailsendform(forms.Form): # ye data database me save nahi hai
    name=forms.CharField()
    email=forms.EmailField()
    to =forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
#for comment
from blog.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
