from django.shortcuts import render, redirect
from . import models
from projects.models import Project
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import ProfileUpdateForm, SkillForm
from django.db.models import Q

# Create your views here.
def profiles(request):
	query = ''
	users = models.Profile.objects.all()
	if request.GET.get('text'):
		query = request.GET.get('text')
		skills = models.Skill.objects.filter(name__icontains = query)
		print(skills)
		users = models.Profile.objects.distinct().filter(
			Q(description__icontains = query) | 
			Q(location__icontains = query) |
			Q(short_description__icontains = query) | 
			Q(github_link__icontains = query)|
			Q(skill__in = skills) |
			Q(user__username__icontains = query) 
			)

	
	
	return render(request, 'users/profile.html', {'users' : users})

@login_required(login_url='LoginRegister')
def userProfile(request, pk):
	user = models.Profile.objects.get(id = pk)
	#print(user, ' ', user.user)
	print()
	otherSkills = []

	for sk in user.skill_set.all():
		if sk.text == None:
			otherSkills.append(sk)

	return render(request, 'users/user_profile.html', {'user' : user, 'otherSkills' : otherSkills})

def loginRegister(request):
	page = 'login'
	print(request.POST)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['userPassword']

		user = authenticate(username = username, password = password)
		if user is not None:
			print("Success")
			login(request, user)
			return redirect('Profile')
		else:
			messages.error(request, 'Username or Password invalid')

	return render(request, 'users/login_register.html', {'page' : page})

def registerUser(request):
	page = 'signUp'
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, 'User Created')
			login(request, user)
			return redirect('UserProfile', pk=user.id)
	return render(request, 'users/login_register.html', {'page' : page, 'form' : form})

def logoutUser(request):
	logout(request)
	return redirect('Profile')

def userAccount(request):
	user = models.Profile.objects.get(user = request.user)
	skills = user.skill_set.all()
	return render(request, 'users/user_account.html', {'user' : user, 'skills' : skills})

def accountUpdate(request):
	user = request.user
	form = ProfileUpdateForm(instance = user.profile)
	print(form)
	if request.method == 'POST':
		form = ProfileUpdateForm(request.POST, request.FILES, instance = user.profile)
		if form.is_valid():
			print(form.cleaned_data['profilePicture'])
			user.profile.description = form.cleaned_data['description']
			user.profile.short_description = form.cleaned_data['description']
			user.profile.location = form.cleaned_data['location']
			user.profile.profilePicture = form.cleaned_data['profilePicture']
			user.profile.save()
			print('success')
			return redirect('UserAccount')
	print('Not Done')
	return render(request, 'users/account_update.html', {'form' : form})

def addSkill(request):
	user = request.user
	form = SkillForm()
	page = 'add'
	if request.method == 'POST':
		form = SkillForm(request.POST)
		skill = form.save(commit = False)
		skill.user = user.profile
		skill.save()
		return redirect('UserAccount')

	return render(request, 'users/skill_form.html', {'form' : form, 'page' : page})

def updateSkill(request, pk):
	page = 'update'
	sk = models.Skill.objects.get(id = pk)
	form = SkillForm()

	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect('UserAccount')
	return render(request, 'users/skill_form.html', {'form' : form, 'page' : page})	






