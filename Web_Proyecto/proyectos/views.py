from django.shortcuts import render
from .models import Proyecto

# Create your views here.

def proyectos (request):
    proyectos =  Proyecto.objects.all()
    return render(request, "proyectos/proyectos.html", {'proyectos': proyectos})

