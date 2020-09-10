from django.urls import path

from . import views

app_name='main'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('list_view/<int:id>-<slug:name>/', views.list_view, name='list_view'),

    # Teste Bootstrapping
    path('matheus/', views.matheus, name='math'),
]
