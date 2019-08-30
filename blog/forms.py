from django import forms
from . import CommentForm

class CommentForm(forms.Form):
	author = forms.CharField(
		max_lenght=60,
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": "Your Name"
			})
	)
	body = forms.CharField(widget=forms.Textarea(
		attrs={
		"class": "form-control",
		"placeholder": "Leave a comment!"
		})
	)