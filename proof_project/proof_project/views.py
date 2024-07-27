from django.http import HttpResponse
from django.template import Template 
from django.template import Context 
import datetime


#This is the index view/landing page
def index(request):
    index_template = open("proof_project/templates/index.html")
    template = Template(index_template.read())
    index_template.close()
    ctx = Context()

    document_rendered = template.render(ctx)

    return HttpResponse(document_rendered)


def close(resquest):
    
    return HttpResponse("Session closed")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    
    return HttpResponse(html)


def age_of_user(resquest, age, year):
    period = year - 2024
    future_age = age + period
    view = "<html><body>In %s you will be %s years old.</body></html>" % (year, future_age)

    return HttpResponse(view)