function loadPagina(url, capa) {
			
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

function removedialogo(dialogo){
	$('#'+dialogo).remove();
}

function mayusculas(nombre) {
    var x = document.getElementById(nombre);
    x.value = x.value.toUpperCase();
}

function numerospuntos(event){
	
	 if(event.shiftKey)
	   {event.preventDefault();}
	 
	   if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 190 || event.keyCode == 110 ||  event.keyCode == 9 || event.keyCode == 39  || event.keyCode == 37)    {
	   }
	   else {
		   if (event.keyCode < 95) {
	          if (event.keyCode < 48 || event.keyCode > 57) { event.preventDefault();
	          }
	        } else {
	              if (event.keyCode < 96 || event.keyCode > 105) {event.preventDefault();}
	        }
	      }
}


function numerosguion(event){
 //alert( event.keyCode);
	if(event.shiftKey)
	{
	     event.preventDefault();
	}

	if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 189 || event.keyCode == 109  || event.keyCode == 9 || event.keyCode == 39  || event.keyCode == 37 )    {
	}
	else {
	     if (event.keyCode < 95) {
	       if (event.keyCode < 48 || event.keyCode > 57  ) {
	             event.preventDefault();
	       }
	     } 
	     else {
	           if (event.keyCode < 96 || event.keyCode > 105) {
	               event.preventDefault();
	           }
	     }
	   }
}



