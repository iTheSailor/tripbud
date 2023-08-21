from django import forms
from .models import Post, Comment
from django.forms import fields, widgets


class PostForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}))
    text_content = forms.CharField(label="",required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Text goes here!!!', 'rows':'4', 'cols':'50'}))
    image = forms.ImageField(label="", required=False, widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Post
        fields = ['title', 'text_content', 'image']

class CommentForm(forms.ModelForm):
    body= forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Text goes here!!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ['body']