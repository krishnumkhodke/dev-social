from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
	path('', views.projects, name = 'Projects'),
	path('project/<str:pk>', views.singleProject, name = 'SingleProject'),
	path('create/', views.createProject, name = 'CreateProject'),
	path('project/update/<int:pk>', views.updateProject, name = 'UpdateProject'),
	path('project/delete/<int:pk>', views.deleteProject, name = 'DeleteProject'),
]