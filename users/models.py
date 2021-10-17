from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, blank = True, null = True)
	description = models.TextField(max_length = 500, blank = True, null = True)
	short_description = models.TextField(max_length = 500, blank = True, null = True)
	location = models.TextField(max_length = 500, blank = True, null = True)
	profilePicture = models.ImageField(default = 'profiles/default_profile.png', upload_to = 'profiles/')
	github_link = models.CharField(max_length = 1000, blank = True, null = True)

	def __str__(self):
		if self.user:
			return self.user.username
		else:
			return 'inv'

class Skill(models.Model):
	user = models.ForeignKey(Profile, on_delete = models.CASCADE, blank = True, null = True)
	name = models.CharField(max_length=100)
	text = models.CharField(max_length = 500, blank=True, null = True)




def profileCreated(sender, instance, created, **kwargs):
	if created:
		user = instance
		profile = Profile.objects.create(user = user)

post_save.connect(profileCreated, User)
