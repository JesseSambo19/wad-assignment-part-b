from django.urls import path
from . import views

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("create/", views.create, name="create"),
path("view/", views.view, name="view"),
path("delete/<str:pk>/", views.delete, name="delete"),
path('update_task/<str:pk>/', views.updateTask, name="update_task"),
]

