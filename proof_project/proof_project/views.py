from django.http import HttpResponse
from django.template import Template 
from django.template import Context 
import datetime
from django.template.loader import get_template
from django.shortcuts import render

class User(object):

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

#This is the index view/landing page
def index(request):

    user = User("John", "Doe")
    greeting = "Hello, welcome to the proof project, "
    dot = user.name + " " + user.last_name + "."
    subjects = ["Python", "Django", "HTML", "CSS", "JavaScript", "SQL", "Git", "GitHub", "Heroku", "Linux", "Bash", "Docker"]
    date= datetime.datetime.now()
    ctx = {"greeting": greeting, "dot": dot, "date": date, "topics": subjects}
    #template = get_template("index.html")
    #document_rendered = template.render(ctx)

    return render(request, "index.html", ctx)


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