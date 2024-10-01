from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import connection
# Create your views here.


class HomeView(TemplateView):
    template_name = 'tree_menu_app/home.html'