from django.shortcuts import render

def principal (request):

    perfil=request.GET.get("perfil")
    
 
    return  render(request,"principal2.html",{'perfil': perfil})
