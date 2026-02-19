from django.shortcuts import render, HttpResponse
from webempresa.webconfig.Query import SQL
import json

def listclientes (request):
    return  render(request,"clientes.html")

def verClientes(request):
       
       osql=SQL()
       lista = osql.listarJSON("exec dbo.sp_ver_cliente ")
   
       return  HttpResponse(json.dumps(lista))
def verificar(request):
       
       id_cliente=request.GET.get("id_cliente")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.sp_verificar_cliente @id_cliente={0} ".format(id_cliente))
   
       return  HttpResponse(json.dumps(lista))

def cliente_mantenimiento(request):
               
    id_cliente  =request.GET.get("id_cliente")
    flag =request.GET.get("flag")

   
    if flag=='3':
              razon_social = ""
              direccion     = ""
              planta_cliente = ""    
              telefono      = ""
              email        = ""
              ruc           = ""
              
    else:
              razon_social   =request.GET.get("razon_social")
              direccion      =request.GET.get("direccion")
              planta_cliente =request.GET.get("planta_cliente")    
              telefono       =request.GET.get("telefono")
              email          = request.GET.get("email")
              ruc            =request.GET.get("ruc")
         
  
    odasql=SQL()
    nregistros=odasql.enviarTransaccion("exec sp_mantenimiento_cliente @id_cliente='{0}' ,"
                                        "@razon_social='{1}',@direccion='{2}',@planta_cliente='{3}',"
                                        "@telefono='{4}',@email='{5}',@ruc='{6}',"
                                        "@flag='{7}'".format(id_cliente,razon_social,direccion,planta_cliente,telefono,email,ruc,flag))
    return HttpResponse(nregistros)
       
def mostrarcliente(request):
       
       id_cliente=request.GET.get("id_cliente")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.sp_mostrar_cliente @id_cliente={0} ".format(id_cliente))
   
       return  HttpResponse(json.dumps(lista))


def listproductos (request):
    return  render(request,"productos.html")
