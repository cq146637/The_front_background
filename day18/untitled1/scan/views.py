from django.shortcuts import render
from scan import models

# Create your views here.


def add(request):
    if request.method == "GET":
        return  render(request,"scanner_website/add.html")
    if request.method =="POST":
        dic = {}
        dic["name"] = request.POST.get("name",None)
        dic["url"] = str(request.POST.get("url",None))
        if not models.website.objects.filter(**dic).first():
            models.website.objects.create(**dic)

        return render(request, "scanner_website/add.html")
