"""
URL routing schema for {{ cookiecutter.application_name }}.

"""

from django.urls import path

from . import views

app_name = "{{ cookiecutter.application_slug }}"

urlpatterns = [
    path('example', views.example, name='example'),
]
