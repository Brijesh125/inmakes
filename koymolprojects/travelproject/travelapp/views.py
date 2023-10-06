from django.shortcuts import render
from .models import Place
from .models import Team


def demo(request):
    obj=Place.objects.all()
    kkp=Team.objects.all()
    return render(request, "index.html",{'result':obj,'kkpp':kkp})

