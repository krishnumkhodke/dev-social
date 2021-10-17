from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from datetime import datetime
# Create your models here.

class Project(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
	title = models.CharField(max_length = 100)
	desciption = models.TextField(null = True, blank = True)
	created = models.DateTimeField(default = datetime.now)
	source_link = models.CharField(max_length = 3500, null = True, blank = True)
	demo_link = models.CharField(max_length = 3500, null = True, blank = True)
	upvotes = models.IntegerField(default = 0)
	downvotes = models.IntegerField(default = 0)
	tags = models.ManyToManyField('Tag')
	img = models.ImageField(blank=True, null = True, default = 'default.png')

	def __str__(self):
		return self.title

class Review(models.Model):
	veridct = (('up' , 'up vote'), ('down', 'down vote'))
	
	project = models.ForeignKey(Project, on_delete = models.CASCADE)
	body = models.TextField()
	created = models.DateTimeField(default = datetime.now)
	vote = models.CharField(max_length = 15, choices = veridct)

	def __str__(self):
		return self.project.title

class Tag(models.Model):
	name = models.CharField(max_length = 100)
	#eated = models.DateTimeField(default = datetime.now)

	def __str__(self):
		return self.name