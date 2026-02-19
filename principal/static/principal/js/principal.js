	jQuery(function($) {
			   $('#sidebar2').insertBefore('.page-content');
			   $('.navbar-toggle[data-target="#sidebar2"]').insertAfter('#menu-toggler');   
			   $(document).on('settings.ace.two_menu', function(e, event_name, event_val) {
				 if(event_name == 'sidebar_fixed') {
					 if( $('#sidebar').hasClass('sidebar-fixed') ) {
						$('#sidebar2').addClass('sidebar-fixed');
						$('#navbar').addClass('h-navbar');
					 }
					 else {
						$('#sidebar2').removeClass('sidebar-fixed')
						$('#navbar').removeClass('h-navbar');
					 }
				 }
			   }).triggerHandler('settings.ace.two_menu', ['sidebar_fixed' ,$('#sidebar').hasClass('sidebar-fixed')]);

			   //menu clientes//
			   $(".sub_verclientes").click(function() {
				
					removedialogo('dialog_addClienteeditcliente');
					removedialogo('dialog_editClienteeditcliente');
					removedialogo('dialoggrabaclientenuevocliente');
					loadPagina("/registro/verClientes","contenido-html");
				
				});
				// cierra clientes

				// menu productos**//

				$(".sub_verproductos").click(function() {
					removedialogo('dialog_editProducto');
					removedialogo('dialog-eliminareditprodu');
					removedialogo('dialog-eliminareditprodu-validar');
					removedialogo('dialoggrabaproducto');
					
					
					loadPagina("/registro/verProductos","contenido-html");
				});

				// cierra productos//

				$( ".sub_ingresodiario" ).click(function() {
			   		
					removedialogo('dialog_ediTmpDetalleFacgenfac');
			   		removedialogo('dialog-eliminargenfac');
			   	    removedialogo('dialog_AgregarNuevoIngreso');
					   		
		  			loadPagina("/beneficio/verIngreso","contenido-html");
		  			
				});

				$( ".sub_montoingreso" ).click(function() {
					
					removedialogo('dialog_ediTmpDetalleFacgenfac');
			   		removedialogo('dialog-eliminargenfac');
			   	    removedialogo('dialog_AgregarNuevoIngreso');
		   			   		
			 		loadPagina("/beneficio/verMontodiario","contenido-html");
		 			
				});

				$( ".sub_montoegreso" ).click(function() {
					
					removedialogo('dialog_ediTmpDetalleFacgenfac');
			   		removedialogo('dialog-eliminargenfac');
			   	    removedialogo('dialog_AgregarNuevoIngreso');
					
		 			loadPagina("/beneficio/verMontoEgresoDiario","contenido-html");
	 			
			     });

				 $(".sub_rptingresodiario").click(function() {
					
					loadPagina("/beneficio/verRptIngresodiario","contenido-html");
				});
	
				$( ".sub_rptbeneficio" ).click(function() {
					
					removedialogo('dialog_ediTmpDetalleFacgenfac');
			   		removedialogo('dialog-eliminargenfac');
			   	    removedialogo('dialog_AgregarNuevoIngreso');
					
   			   		
		 			loadPagina("/beneficio/rptbeneficio","contenido-html");
	 			
			     });

				 $( ".sub_rptingresoegreso" ).click(function() {
					
					removedialogo('dialog_ediTmpDetalleFacgenfac');
			   		removedialogo('dialog-eliminargenfac');
			   	    removedialogo('dialog_AgregarNuevoIngreso');
					
   			   		
		 			loadPagina("/beneficio/rptingresoegreso","contenido-html");
	 			
			     });

			   				   				   				
				$(".sub_reportemensual").click(function() {
					loadPagina("/sgpc/app/principal/generarreporte","contenido-html");
				});
				
								
				//lucho
				
				
				
				$( ".sub_hielodiario" ).click(function() {
			   		
					removedialogo('dialog_ediTmpDetalleFacgenfacHielo');
			   		removedialogo('dialog-eliminargenfacHielo');
			   	    removedialogo('dialog_AgregarNuevoIngresoHielo');
					   		
		  			loadPagina("/sgpc/app/principal/hielodiario","contenido-html");
		  			
				});
				
								
				
	
			})
			
			$(document).ready(function() {
				jQuery.extend(jQuery.validator.messages, {
				  required: "Este campo es obligatorio.",
				  remote: "Por favor, rellena este campo.",
				  email: "Por favor, escribe una direcci�n de correo v�lida",
				  url: "Por favor, escribe una URL v�lida.",
				  date: "Por favor, escribe una fecha v�lida.",
				  dateISO: "Por favor, escribe una fecha (ISO) v�lida.",
				  number: "Por favor, escribe un n�mero entero v�lido.",
				  digits: "Por favor, escribe s�lo d�gitos.",
				  creditcard: "Por favor, escribe un n�mero de tarjeta v�lido.",
				  equalTo: "Por favor, escribe el mismo valor de nuevo.",
				  accept: "Por favor, escribe un valor con una extensi�n aceptada.",
				  maxlength: jQuery.validator.format("Por favor, no escribas m�s de {0} caracteres."),
				  minlength: jQuery.validator.format("Por favor, no escribas menos de {0} caracteres."),
				  rangelength: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1} caracteres."),
				  range: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1}."),
				  max: jQuery.validator.format("Por favor, escribe un valor menor o igual a {0}."),
				  min: jQuery.validator.format("Por favor, escribe un valor mayor o igual a {0}.")
				});
			});
