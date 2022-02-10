from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def index(request):
    template = loader.get_template("cms/feed.html")
    context = {}
    return HttpResponse(template.render(context, request))