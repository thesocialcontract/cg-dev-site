from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def index(request):
    template = loader.get_template("top/index.html")
    context = {}
    return HttpResponse(template.render(context, request))