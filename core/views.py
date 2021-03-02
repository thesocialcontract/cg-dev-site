from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("base.html")
    context = {
        "variable": "foobar I'm injecting variables",
    }
    return HttpResponse(template.render(context, request))