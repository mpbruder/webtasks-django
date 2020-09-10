from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

app_name='register'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sign-up/', views.register, name='sign-up'),
    path('login/', views.myLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main:home'), name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]