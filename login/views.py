from django.shortcuts import render
from  webempresa.webconfig.Query import SQL
from django.http import HttpResponse
import json

def login (request):
    return  render(request,"login.html")
   
def validaruser(request):
       
    usuario=request.GET.get("usuario")
    clave=request.GET.get("clave")
    osql=SQL()
    lista = osql.listarJSON("exec dbo.sp_valida_user @usuario='{0}', @clave='{1}'".format(usuario,clave))
    return  HttpResponse(json.dumps(lista))
       


# Create your views here.
