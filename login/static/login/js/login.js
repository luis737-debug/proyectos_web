  
function ingresar(){
  
    var usuario=$("#txtusuario").val();
    var clave=$("#txtclave").val();

    valor="usuario="+usuario+"&clave="+clave;

      $.ajax({
          type : 'get',
          data:valor,
          dataType : 'json',
          url :'./validar',
          //url :'/login/validar?usuario='+usuario+'&clave='+clave,
           beforeSend: function(){
              
                  //$("#div_tabla_c1").html("<img src='{% static 'css/graphics/loader.white.gif'></img>");
                  
                },
          success : function(result) {
              var json =result;	
                
            var perfil;

                 $.each(json, function(j, resultgenfac) {

                        perfil=resultgenfac['perfil'];
                    });

                   // alert(perfil);

                if (json.length>0)
					{             
                   
                        window.location = '/principal/principal?perfil='+perfil;	

                        //loadPagina2("/principal/principal","main-principal");
					
					}
				else {
                   
                    $("#txtusuario").val("");
                    $("#txtclave").val("");


                    $("#mensaje").html("<span style='color:red'>Error de Usuario/Clave</span>");
                     }                                 
          },
          
          error : function(xhr, ajaxOptions, thrownError) {
              alert(xhr.status + ' ' + thrownError);
          }
      });

 }
function loadPagina2(url, capa) {
			
			  $.ajax({
					type		: 'get',
					dataType	: 'html',
					url			: url,
					async		: false,
					success		: function(result) {
						
						$("#" + capa).html(result);
					},
					error 		: function(xhr, ajaxOptions, thrownError) {
						$.jError(xhr.status, 'Error');
						$.jError(thrownError, 'Error');
					}
				});
   
}

