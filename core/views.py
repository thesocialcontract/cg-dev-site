from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def index(request):
    template = loader.get_template("core/index.html")
    context = {
        "year": datetime.now().year
    }
    return HttpResponse(template.render(context, request))

def julia(request):
    template = loader.get_template("heart.html")
    context = {}
    return HttpResponse(template.render(context, request))