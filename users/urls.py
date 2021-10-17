from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.profiles, name = 'Profile'),
    path('/<int:pk>', views.userProfile, name = 'UserProfile'),
    path('/login/', views.loginRegister, name = 'LoginRegister'),
    path('/signup/', views.registerUser, name = 'RegisterUser'),
    path('/logout/', views.logoutUser, name = 'LogoutUser'),
    path('/account/', views.userAccount, name = 'UserAccount'),
    path('/account/update/', views.accountUpdate, name = 'AccountUpdate'),
    path('/skill/', views.addSkill, name = 'AddSkill'),
    path('/update/skill/<int:pk>', views.updateSkill, name = 'UpdateSkill'),
] 

