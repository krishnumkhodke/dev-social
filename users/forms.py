from django.forms import ModelForm
from . import models

class ProfileUpdateForm(ModelForm):
	class Meta:
		model = models.Profile
		exclude = ['user']

class SkillForm(ModelForm):
	class Meta:
		model = models.Skill
		exclude = ['user']
	#for name, field in self.fields.items():
	#		field.widget.attrs.update({'class': 'input'})