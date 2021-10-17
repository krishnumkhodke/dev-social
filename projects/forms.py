from django.forms import ModelForm, widgets
from . import models
from django import forms
from django.db.models.base import Model


class ProjectCreationForm(ModelForm):
	class Meta:
		model = models.Project
		exclude = ['created', 'upvotes', 'downvotes']

		widgets = {
			'tags': forms.CheckboxSelectMultiple(),
		}

	def __init__(self, *args, **kwargs):
		print('Hello')
		super(ProjectCreationForm, self).__init__(*args, **kwargs)

		for name, field in self.fields.items():
			field.widget.attrs.update({'class': 'input'})