from django.contrib import admin
from django.urls import path
from beneficio import views

urlpatterns = [
    path('verIngreso/',views.ingresodiario),
    path('listarDetalleIngreso/',views.listadetalleingreso),
    path('comboPnroductoIngreso/',views.comboPnroductoIngreso),
    path('comboCliente2/',views.comboCliente2),
    path('calculo/',views.calculoresumen),
    path('grabaringreso/',views.beneficio_mantenimiento),
    path('mostraringresodet/',views.listaregistroingreso),
    
    path('verMontodiario/',views.montoingresodiario),
    path('listarDetalleMontoIngreso/',views.listadetallemontoingreso),
    path('grabarmontoingreso/',views.beneficio_montomantenimiento),
    path('calculo_ingreso/',views.calculomontoingresoresumen),
    path('mostrarmontoingresodet/',views.listaregistromontoingreso),

    path('verMontoEgresoDiario/',views.montoEgresodiario),
    path('comboCliente2Egreso/',views.comboCliente2Egreso),
    path('listarDetalleMontoEgreso/',views.listadetallemontoEgreso),
    path('calculo_egreso/',views.calculomontoegresoresumen),
    path('grabarmontoegreso/',views.beneficio_montoegresomantenimiento),
    path('mostrarmontoegresodet/',views.listaregistromontoegreso),

    path('verRptIngresodiario/',views.rptingresodiario),
    path('rptbeneficio/',views.rptbeneficiosemanal),
    path('zRptBeneficio/',views.rptlistabeneficiosemanal),
    path('rptingresoegreso/',views.rptingresoegreso),
    path('listaringresoegreso/',views.rptlistaingresoegreso),
    path('calculo_ingresoegreso/',views.calculomontoingresoegreso),


]   