from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def vistaUno(request):
    html="""
    <h1 style="color:blue">hola mundo app1</h1>
    <h2 style="color:red">suck my dick</h2>
    """
    return HttpResponse(html)
