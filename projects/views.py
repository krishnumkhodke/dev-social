from django.shortcuts import render, redirect
from . import models
from .forms import ProjectCreationForm
from django.db.models import Q



# Create your views here.
#1
def singleProject(request, pk):
	try:
		project = models.Project.objects.get(title = pk)
	except:
		project = None
	tags = []
	if project:
		tags = project.tags.all()
	return render(request, 'projects/single_project.html', {'project' : project , 'tags' :tags})

def projects(request):
	query = ''
	projects = models.Project.objects.all();
	
	if request.GET.get('text'):
		query = request.GET.get('text')
		tags = models.Tag.objects.filter(name__icontains = query)
		projects = models.Project.objects.distinct().filter(
			Q(title__icontains = query) | 
			Q(desciption__icontains = query) |
			Q(user__username__icontains = query) |
			Q(tags__name__icontains = query)
			)
	
	return render(request, 'projects/projects.html', {'projects':projects})

def createProject(request):

	user = request.user
	form = ProjectCreationForm()

	if request.method == 'POST':
		form = ProjectCreationForm(request.POST, request.FILES)
		if form.is_valid():
			pr = form.save(commit = False)
			pr.user = user
			pr.save()
			return redirect('Projects')
	return render(request, 'projects/create_project.html', {'form' : form})


def updateProject(request, pk):
	try:
		project = models.Project.objects.get(title = pk)
	except:
		project = None
	form = ProjectCreationForm(instance = project)

	if request.method == 'POST':
		form = ProjectCreationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('Projects')
	else:
		form = ProjectCreationForm(instance = project)
	return render(request, 'projects/create_project.html', {'form' : form})


def deleteProject(request, pk):
	project = models.Project.objects.get(title = pk)
	if request.method == 'POST':
		project.delete()
		return redirect('Projects')

	return render(request, 'projects/deleteProject.html')