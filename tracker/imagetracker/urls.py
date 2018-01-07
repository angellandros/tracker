from django.urls import path

from . import views

urlpatterns = [
    path('<str:hash>', views.image, name='image'),
]