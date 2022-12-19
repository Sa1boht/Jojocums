"""Jojocums URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

import accounts

app_name = "Jojocums"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("jogo/create_jogo", views.create_jogo, name="create_jogo"),
    path("jogo/edit/<int:jogo_id>", views.edit_jogo, name="edit_jogo"),
    path("jogo/delete/<int:jogo_id>", views.delete_jogo, name="delete_jogo"),
    path("jogo/jogos", views.jogo_list, name="jogos"),
    path("accounts/", include("accounts.urls")),
]
