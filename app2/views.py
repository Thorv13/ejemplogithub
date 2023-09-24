from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def vistaDos(request):
    html="""
    <h1 style="color:blue">hola mundo app2</h1>
    <h2 style="color:red">suck my dick X2 </h2>
    """
    return HttpResponse(html)
