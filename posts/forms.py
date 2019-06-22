from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 1}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Post
        fields = ['title', 'content']
