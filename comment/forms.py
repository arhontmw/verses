from django import forms
from .models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        fields = ("text",)
