from django.shortcuts import render, HttpResponse
from webempresa.webconfig.Query import SQL
import json

def ingresodiario (request):
    return  render(request,"IngresoDiario.html")




def listadetalleingreso(request):
       
       fecha_ingreso=request.GET.get("fecha_ingreso")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.SP_listar_detalle_ingreso @fecha_ingreso='{0}' ".format(fecha_ingreso))
     
       return  HttpResponse(json.dumps(lista))

def listadetallemontoingreso(request):
       
       fecha_ingreso=request.GET.get("fecha_ingreso")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.SP_listar_detalle_monto_ingreso @fecha_ingreso='{0}' ".format(fecha_ingreso))
     
       return  HttpResponse(json.dumps(lista))

def comboPnroductoIngreso(request):
       
       osql=SQL()
       lista = osql.listarJSON("exec dbo.sp_combo_producto_planta ")
     
       return  HttpResponse(json.dumps(lista))

def comboCliente2(request):
       
       osql=SQL()
       lista = osql.listarJSON("exec dbo.sp_combo_cliente_planta ")
     
       return  HttpResponse(json.dumps(lista))

def calculoresumen(request):
       
       fecha=request.GET.get("fecha")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.total_detalle_ingreso @fecha='{0}' ".format(fecha))
     
       return  HttpResponse(json.dumps(lista))

def beneficio_mantenimiento(request):
               
    id_ingreso  =request.GET.get("id_ingreso")
    flag =request.GET.get("flag")

  
  
    if flag=='3':
              txtfechaingreso    =""    
              cmbclienteingreso  =0  
              txtcantidadingreso =0    
              cmbproductoingreso =0
              txtprecuniingreso  =0    
              cantidaddet        =" Ç"  
              
    else:
              txtfechaingreso    =request.GET.get("txtfechaingreso")
              cmbclienteingreso  =request.GET.get("cmbclienteingreso")
              txtcantidadingreso =request.GET.get("txtcantidadingreso")    
              cmbproductoingreso =request.GET.get("cmbproductoingreso")
              txtprecuniingreso  = request.GET.get("txtprecuniingreso")
              cantidaddet        =request.GET.get("txtcantidadingresodet")
         
  
    odasql=SQL()
    nregistros=odasql.enviarTransaccion("exec sp_mantenimiento_ingreso_diario @id_ingreso='{0}' ,"
                                        "@txtfechaingreso='{1}',@cmbclienteingreso='{2}',@txtcantidadingreso='{3}',"
                                        "@cmbproductoingreso='{4}',@txtprecuniingreso='{5}',@flag='{6}',"
                                        "@cantidaddet='{7}'".format(id_ingreso,txtfechaingreso,cmbclienteingreso,txtcantidadingreso,cmbproductoingreso,txtprecuniingreso,flag,cantidaddet))
    return HttpResponse(nregistros)

def listaregistroingreso(request):
       
       id_ingreso=request.GET.get("id_ingreso")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.SP_listar_detalle_ingreso_Reg @id_ingreso='{0}' ".format(id_ingreso))
     
       return  HttpResponse(json.dumps(lista))


def montoingresodiario (request):
    return  render(request,"MontoIngresoDiario.html")

def beneficio_montomantenimiento(request):
               
    id_ingreso  =request.GET.get("id_ingreso")
    flag =request.GET.get("flag")

              
    if flag=='3':
              txtfechaingreso    =""    
              cmbclienteingreso  =0  
              txtcantidadingreso =0   
              cantidaddet        =""   
              nroboleta          =""
                        
    else:
              txtfechaingreso    =request.GET.get("txtfechaingreso")
              cmbclienteingreso  =request.GET.get("cmbclienteingreso")
              txtcantidadingreso =request.GET.get("txtcantidadingreso") 
              cantidaddet        =request.GET.get("txtcantidadingresodet")   
              nroboleta          =request.GET.get("txtnroboleta")
             
    odasql=SQL()
    nregistros=odasql.enviarTransaccion("exec sp_mantenimiento_ingreso_monto_diario @id_ingreso='{0}' ,"
                                        "@txtfechaingreso='{1}',@cmbclienteingreso='{2}',@txtcantidadingreso='{3}',"
                                        "@cantidaddet='{4}',@nroboleta='{5}',@flag='{6}' ".format(id_ingreso,txtfechaingreso,cmbclienteingreso,txtcantidadingreso,cantidaddet,nroboleta,flag))
    return HttpResponse(nregistros)

def calculomontoingresoresumen(request):
       
       fecha=request.GET.get("fecha")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.total_detalle_monto_ingreso @fecha='{0}' ".format(fecha))
     
       return  HttpResponse(json.dumps(lista))

def listaregistromontoingreso(request):
       
       id_ingreso=request.GET.get("id_ingreso")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.SP_listar_detalle_monto_ingreso_Reg @id_ingreso='{0}' ".format(id_ingreso))
     
       return  HttpResponse(json.dumps(lista))


def montoEgresodiario (request):
    return  render(request,"MontoEgresoDiario.html")

def comboCliente2Egreso(request):
       
       osql=SQL()
       lista = osql.listarJSON("exec dbo.sp_combo_egresos_planta ")
     
       return  HttpResponse(json.dumps(lista))

def listadetallemontoEgreso(request):
       
       fecha_ingreso=request.GET.get("fecha_ingreso")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.SP_listar_detalle_monto_egreso @fecha_ingreso='{0}' ".format(fecha_ingreso))
     
       return  HttpResponse(json.dumps(lista))

def calculomontoegresoresumen(request):
       
       fecha=request.GET.get("fecha")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.total_detalle_monto_egreso @fecha='{0}' ".format(fecha))
     
       return  HttpResponse(json.dumps(lista))

def beneficio_montoegresomantenimiento(request):
               
    id_ingreso  =request.GET.get("id_ingreso")
    flag =request.GET.get("flag")

              
    if flag=='3':
              txtfechaingreso    =""    
              cmbclienteingreso  =0  
              txtcantidadingreso =0   
              cantidaddet        =""   
              nroboleta          =""
                        
    else:
              txtfechaingreso    =request.GET.get("txtfechaingreso")
              cmbclienteingreso  =request.GET.get("cmbclienteingreso")
              txtcantidadingreso =request.GET.get("txtcantidadingreso") 
              cantidaddet        =request.GET.get("txtcantidadingresodet")   
              nroboleta          =request.GET.get("txtnroboleta")
             
    odasql=SQL()
    nregistros=odasql.enviarTransaccion("exec sp_mantenimiento_egreso_monto_diario @id_ingreso='{0}' ,"
                                        "@txtfechaingreso='{1}',@cmbclienteingreso='{2}',@txtcantidadingreso='{3}',"
                                        "@cantidaddet='{4}',@nroboleta='{5}',@flag='{6}' ".format(id_ingreso,txtfechaingreso,cmbclienteingreso,txtcantidadingreso,cantidaddet,nroboleta,flag))
    return HttpResponse(nregistros)

def listaregistromontoegreso(request):
       
       id_ingreso=request.GET.get("id_ingreso")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.SP_listar_detalle_monto_egreso_Reg @id_ingreso='{0}' ".format(id_ingreso))
     
       return  HttpResponse(json.dumps(lista))


def rptingresodiario (request):
    return  render(request,"RptIngresoDiario.html")

def rptbeneficiosemanal (request):
    return  render(request,"Rpt_Beneficio.html")

def rptlistabeneficiosemanal(request):
       
       txtfechaini=request.GET.get("txtfechaini")
       txtfechafin=request.GET.get("txtfechafin")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.sp_reporte_beneficio @fechaini='{0}',"
                               "@fechafin='{1}' ".format(txtfechaini,txtfechafin))
     
       return  HttpResponse(json.dumps(lista))

def rptingresoegreso (request):
    return  render(request,"RptIngresoEgreso.html")

def rptlistaingresoegreso(request):
       
       txtfecha=request.GET.get("fecha_ingreso")
       osql=SQL()
       lista = osql.listarJSON("exec dbo.sp_rpt_ingresoegreso @fecha='{0}' ".format(txtfecha))
     
       return  HttpResponse(json.dumps(lista))

def calculomontoingresoegreso(request):
       
       fecha=request.GET.get("fecha")

       osql=SQL()
       lista = osql.listarJSON("exec dbo.total_ingresoegreso @fecha='{0}' ".format(fecha))
     
       return  HttpResponse(json.dumps(lista))



