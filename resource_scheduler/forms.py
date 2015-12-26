from django import forms

class ResourceForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100)
	comment = forms.CharField(label='Comment', widget=forms.Textarea)
