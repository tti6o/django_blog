from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader, Context

class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        return "my name is " + self.name

def index(request):
    t = loader.get_template("index.html")
    user = {"name":"tom","age":23,"sex":"male"}
    book_list = ["python", "ruby", "java", "c"]

    person = Person("jack", 17, "female")
    c = Context({"title": "django", "user": user, "book_list":book_list})
    return HttpResponse(t.render(c))
