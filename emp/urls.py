# -*- coding: utf-8 -*-
from django.urls import path
from emp import views

urlpatterns = [
        path('managers', views.managers, name='managers'),
        path('login', views.login_request, name='login'),
        ]
