from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.project),
    path('', views.snow),
    path('bio/', views.bio),

]
