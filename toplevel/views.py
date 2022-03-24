from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def index(request):
    template = loader.get_template("toplevel/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def http404(request):
    template = loader.get_template("404.html")
    context = {}
    return HttpResponse(template.render(context, request))

def http500(request):
    template = loader.get_template("500.html")
    context = {}
    return HttpResponse(template.render(context, request))