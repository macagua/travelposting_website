(function(){
	window.uniqid = function(){
		function rand(){
			  return "xxxx_xxxx_xxxx_xxxx_xxxx".replace(/[xy]/g, function(c) {
				var r = Math.random() * 16 | 0, v = c == "x" ? r : (r & 0x3 | 0x8);
				return v.toString(16);
			  });
		}
		return "node_" + rand();
	};

	window.isFunction = function(o){

		return Function.prototype.isPrototypeOf(o);
	};

	window.isElementNode = function(o){
		if($.isEmptyObject(o))

			return false;

		if($.isEmptyObject(o))
			return false;
		try{
			var obj = $(o)[0];
			return obj.nodeType === Node.ELEMENT_NODE  ? true : false;
		}
		catch(e){
			return false;
		}
	};

	window.isElementText = function(o, noEmpty){
		if(typeof o === 'string'  || typeof o === 'number' ){
			if(typeof noEmpty == 'undefined')
				return true;

			if(o.toString().length > 0)
				return true;
		}

		return false;
	};

	window.isBoolean = function (o){
		if(typeof o == 'boolean')
			return true;
		else
			return false;
	};

	(function(){
		function domModal(){
			var obj = {};

			obj.icon = (function(){
				var e = $('<i>');
				return e;
			})();

			obj.title = (function(){
				var e = $('<span>');
				return e;
			})();

			obj.header = (function(){

				var e = $('<div>');

				e.btnClose = $('<button>').attr({
					'type'  : 'button',
					'class' : 'close',
					'data-dismiss' : 'modal',
				}).html('&times;');

				(function(){
					e.append(e.btnClose);

					$('<h4>')
						.addClass('modal-title')
						.append(obj.icon)
						.append(obj.title)
						.appendTo(e);
				})();

				return e;
			})();

			obj.body = (function(){
				var e = $('<div>');
				return e;
			})();

			obj.footer = (function(){

				var e = $('<div>')
					.addClass('modal-footer');
				return e;
			})();

			obj.content = (function(){

				var e = $('<div>')
					.append(obj.header)
					.append(obj.body)
					.append(obj.footer);

				return e;
			})();

			obj.dialog = (function(){
				var e = $('<div>')
					.append(obj.content);
				return e;
			})();

			obj.bsModal = (function(){
				var e = $('<div>')
					.attr('id',   uniqid())
					.attr('role', 'dialog')
					.html(obj.dialog);
				return e;
			})();

			obj.addLoader = function( callback ){

				if(obj.content.find('[role="loader"]').length > 0)
					return;


				if( obj.bsModal.is(':visible') == 0 )
				{
					obj.reset('css');
					obj.reset('content');
					obj.header.hide();
					obj.footer.hide();
					obj.open();
				}

				if(obj.body.innerHeight() < 320)
					obj.body.addClass('modal-body-loader').show();

				$(obj.content)
					.addLoader( callback );
			};

			obj.rmLoader = function( callback ){

				var _callback = function(){

					obj.body.removeClass('modal-body-loader');

					if(isFunction(callback))
						callback();
				};

				$(obj.content)
					.rmLoader(_callback);
			};

			obj.open = function(){

				if(obj.bsModal.is(':visible') == false)
				{
					$('body').prepend(obj.bsModal);
					obj.bsModal.modal({
						'backdrop' : 'static',
						'keyboard' : true,
					});
				}
			};

			obj.hide = function(){
				obj.content.addClass("fade");
			};

			obj.show = function(){
				obj.content.addClass("fade in");
			};

			obj.fail = function(titleError, msnError, btnCloseTitle, closeCallBack){

				var msnError = $('<p>')
					.html(msnError);

				var btnClose = $('<button>').attr({
					'class'         : 'btn btn-danger',
					'type'          : 'button',
					'data-dismiss'  : 'modal',
				});

				if(isElementText(btnCloseTitle, true))
					btnClose.text(btnCloseTitle);
				else
					btnClose.html('Ok');

				this.icon.attr('class', 'gallery-icon-error text-danger');
				this.title.attr('class','text-danger');
				this.title.html(titleError);
				this.size('modal-320px');
				this.header.show();

				this.body.html(msnError).show();
				this.footer.html(btnClose).show();

				this.bsModal.off('hide.bs.modal');
				this.bsModal.off('hidden.bs.modal');

				this.bsModal.on('hide.bs.modal', function(e){
					return true;
				});

				this.bsModal.on('hidden.bs.modal', function (e){

					if( isFunction(closeCallBack))
					{
						$(this).remove();
						closeCallBack();
					}
					/*
					else
						window.location.reload(true);
					*/
				});

				obj.open();
			};

			obj.load = function(url, callBack){

				obj.addLoader();
				setTimeout(function(){
					$.ajax({
						url : url,
						data : {'modal-load' : true },
						type : 'get',
						dataType : 'html',
					})
					.done(function(data){
						obj.reset.default(true);
						obj.body.html(data).show();
						obj.rmLoader();

						if(typeof callBack != 'undefined' && isFunction(callBack) )
							callBack();
					})
					.fail(function(data){
						var prevUrl = this.url;

						switch(data.status)
						{
							case 0:
							case 302:
								window.location.reload(true);
								return;

							default:
								obj.fail(data.status, data.responseText);
								obj.rmLoader();
								return;
						}
					});
				}, 200);
			};

			obj.close = function(){

				if(obj.bsModal.is(':visible') == true)
					obj.bsModal.modal('hide');
			};

			obj.remove = function(overload){
				obj.close();

				overload = overload || false;

				obj.registerEvent('afterClose', function(){
					obj.bsModal.remove();
				}, overload);
			};

			obj.reset = function(param){

				switch(param)
				{
					//
					case 'events':
						obj.bsModal.off("show.bs.modal");
						obj.bsModal.off("shown.bs.modal");
						obj.bsModal.off("hide.bs.modal");
						obj.bsModal.off("hidden.bs.modal");
						break;

					case 'show.bs.modal':
					case 'beforeOpen':
						obj.bsModal.off("show.bs.modal");
						break;

					case 'shown.bs.modal':
					case 'afterOpen':
						obj.bsModal.off("shown.bs.modal");
						break;

					case 'hide.bs.modal':
					case 'beforeClose':
						obj.bsModal.off("hide.bs.modal");
						break;

					case 'hidden.bs.modal':
					case 'afterClose':
						obj.bsModal.off("hidden.bs.modal");
						break;

					//
					case 'css':
						if(obj.bsModal.is(':visible'))
							obj.bsModal.attr('class', 'modal fade in');
						else
							obj.bsModal.attr('class', 'modal fade');

						obj.dialog.attr('class',  'modal-dialog');
						obj.content.attr('class', 'modal-content');
						obj.header.attr('class', 'modal-header');
						obj.header.btnClose.attr('class', 'close');
						obj.icon.removeAttr('class');
						obj.title.removeAttr('class');
						obj.body.attr('class','modal-body');
						obj.footer.attr('class','modal-footer');
						break;

					//
					case 'content':
						obj.icon.html('').removeAttr('class');
						obj.title.html('');
						obj.body.html('');
						obj.footer.html('');
						break;

					case 'icon-content':
						obj.icon.html('').removeAttr('class');
						break;

					case 'title-content':
						obj.title.html('');
						break;

					case 'body-content':
						obj.body.html('');
						break;

					case 'footer-content':
						obj.footer.html('');
						break;
				}
			};

			obj.reset.default = function(forceBodyContent ){

				forceBodyContent = (isBoolean(forceBodyContent)) ? forceBodyContent : false;
				obj.reset("events");
				obj.reset("icon-content");
				obj.reset("title-conten");
				obj.reset("footer-content");
				obj.reset("css");
				obj.body.attr("style", "");

				if(forceBodyContent)
					obj.reset("body-content");
			};

			obj.registerEvent = function(eventName, fn, overload)
			{
				overload = (isBoolean(overload)) ? overload : false;
				switch(eventName)
				{
					case 'show.bs.modal':
					case 'beforeOpen':
						if(overload === true)
							obj.reset(eventName);

						if(isFunction(fn))
							obj.bsModal.on('show.bs.modal', fn);
						break;

					case 'shown.bs.modal':
					case 'afterOpen':
						if(overload === true)
							obj.reset(eventName);

						if(isFunction(fn))
							obj.bsModal.on('shown.bs.modal', fn);
						break;

					case 'hide.bs.modal':
					case 'beforeClose':
						if(overload === true)
							obj.reset(eventName);

						if(isFunction(fn))
							obj.bsModal.on('hide.bs.modal', fn);
						break;

					case 'hidden.bs.modal':
					case 'afterClose':
						if(overload === true)
							obj.reset(eventName);

						if(isFunction(fn))
							obj.bsModal.on('hidden.bs.modal', fn);
						break;
				}
			};

			obj.size = function(sizeClass){

				obj.dialog.attr('class',  'modal-dialog');
				if(isElementText(sizeClass, true))
					obj.dialog.addClass(sizeClass);
			};

			obj.reset('css');
			return obj;
		}

		var modal = new domModal();

		modal.confirm = function(options){

			var m = new domModal();

			var config = {
				size            : 'modal-confirm',
				icon            : 'gallery-icon-confirm',
				title           : 'Confirmación' ,
				confirm         : '¿Desea continuar?',
				labelOk         : 'Si',
				labelCancel     : 'No',
				callbackOk      : function(){},
				callbackCancel  : function(){},
				beforeClose     : function(){},
			};

			$.extend(config, options);
			m.icon.attr('class', config.icon).css('margin-right', '10px');
			m.size(config.size);
			m.title.html(config.title);
			m.header.btnClose.hide();
			m.body.html(config.confirm);

			if(config.labelOk != false)
			{
				var btnOk = $("<button>");
					btnOk.addClass('btn btn-default')
					.html(config.labelOk)
					.on('click', function(e){
						e.preventDefault();
						e.stopPropagation();
						m.registerEvent('afterClose', config.callbackOk);
						m.close();
					}).appendTo(m.footer);
			}

			if(config.labelCancel != false)
			{
				var btnCl = $("<button>");
					btnCl.addClass('btn btn-danger')
					.html(config.labelCancel)
					.on('click', function(e){
						e.preventDefault();
						e.stopPropagation();
						m.registerEvent('afterClose', config.callbackCancel);
						m.close();
					}).appendTo(m.footer);
			}

			if($(".modal").has(':visible').length > 0)
			{
				var _modal = $(".modal").has(':visible').first();
					_modal
						.fadeOut(450)
						.removeClass('fade');

				setTimeout(function(){

					m.bsModal
						.removeClass('fade')
						.appendTo( $('body') )
						.modal({
							'backdrop' : false,
							'keyboard' : false,
						});

					m.registerEvent('afterClose', function(){
						m.bsModal.remove();
						_modal.fadeIn('450' , function(){
							_modal.addClass('fade');
						});
					});

					m.registerEvent('beforeClose', function(){
						config.beforeClose();
					}, true);
				},420);
			}
			else{
				m.bsModal
					.modal({
						'backdrop' : 'static',
						'keyboard' : false,
					});
			}

			m.registerEvent('afterOpen', function(){
				if((config.labelOk == false) && (config.labelCancel == false))
					return;

				if(config.labelCancel != false)
					btnCl.focus();
				else
					btnOk.focus();
			}, true);
		};

		window.modal  = window.modal  || modal;
	})();
})();

(function($){
	$.fn.addLoader = function(callBack){
		var e = $(this);
		if(e.find('[role="loader"]').length  > 0)
			return;

		var parentLoader = $('<div>')
			.attr('role', 'loader')
			.css('border-radius', e.css('border-radius'))
			.html('<i class="loader"></i>')
			.appendTo(e)
			.addClass('loader-container fade in');

			if(isFunction(callBack || null))
				setTimeout(callBack);
	};

	$.fn.rmLoader = function(callBack){
		$(this).find('[role="loader"]').removeClass("in").remove();
		if(isFunction(callBack || null))
			setTimeout(callBack);
	};

	$.fn.gallery = function(options){

		var el = $(this);
		    el.css('min-height', '250px');

		var dGrid  = $('<div>');
		var boxAdd = $('<div>');

		items = [];

		var config = {

			inputFile : {
				name        : 'image',
				maxFiles    : 12,
			},
			inputComment : {
				name : 'description',
			},
			routes : {
				list   : 'list.php',
				create : 'create.php',
 				update : 'update.php',
 				delete : 'delete.php',
			},
			events : {
				afterRender : function(){
					console.log('events.afterRender');
				},

				beforeUpdateComment : function(items,index,element){
					return true;
				},

				afterUpdateComment : function(data){
					console.log(data); // data == reponse jqXHR on done
				},

				errorOnUpdateComment : function(data){
					console.log(data); // data == response jqXHR on fail
				},

				errorOnUploadImage : function(data){
					console.log(data); // data == response jqXHR on fail
				},

				afterUploadImage : function(data){
					console.log(data); // data == response jqXHR on fail
				},

				onMaxImages : function(items){
					console.log(items); // data == response jqXHR on fail
				},

				beforeDelete : function(items,index,element){
					return true;
				},

				afterDelete : function(data){
					console.log(data); // data == reponse jqXHR on done
				},

				errorOnDelete : function(data){
					console.log(data); // data == response jqXHR on fail
				},
				errorOnLoad   : function(data){
					console.log(data); // data == response jqXHR on fail
				},

			},
			labels : {
				'title'           : '',
				'addItem'         : 'Agregar imagenes',
				'rmItem'          : 'Eliminar',
				'addComment'      : 'Escribe un comentario...',
				'viewItem'        : 'Mostrar detalles',
				'confirm'         : {
					'cancel'	: 'No',
					'continue'	: 'Si',
					'title'		: 'Confirmar acción',
					'msn'       : '¿Esta seguro que desea eliminar este registro?',
				},
			}
		};

		$.extend(config, options);
		console.log(config);


		var inputFile = $("<input>").attr({
			type     : 'file',
			multiple : true,
			accept   : 'image/jpeg,image/jpg,image/png',
		});

		function upload(file, src)
		{
		}

		function renderItem(model, index)
		{
			if(typeof index == 'undefined')
				var index = (items.length-1 < 0) ? 0 : items.length-1;

			var dItem = $('<div>');
				dItem
					.addClass('item')
					.css({
						'background-image'    	: 'url('+ model.url.large +')',
						'background-repeat'   	: 'no-repeat',
						'background-position' 	: 'center',
						'background-size'		: 'cover',
						'cursor'				: 'pointer',
					})
					.on('click', function(e){
						e.preventDefault();
						e.stopPropagation();
				    	previewModal(index);
				    })
					.appendTo(dGrid);

			var d1 = $('<div>');
				d1.appendTo(dItem);

			var d2 = $('<div>');
				d2.addClass('actions clearfix text-center')
				.appendTo(dItem);

			var icon = $('<i>');
				icon.addClass('gallery-icon-action gallery-icon-photo')
				    .attr('title', config.labels.viewItem)
				    .appendTo(d2);

			var d3 = $('<div>');
				d3.addClass('textarea-content')
				.appendTo(dItem);

			var imput = $('<textarea>');
				imput.addClass('form-control gallery-textarea-comment');
				imput.text(model.description);
				imput.attr({

					'maxlength'	   : 255,
					'placeholder'  : config.labels.addComment,
				})
				.appendTo(d3)
				.on('click', function(e){
					// evitar open modal cuando le doy click al textarea
					e.preventDefault();
					e.stopPropagation();
				})
				.on("keydown", function(e){
					if(e.keyCode == 13 && !e.shiftKey)
					{
						e.preventDefault();
						$(this).blur();
					}
				})
				.on('change', function(e){
					e.preventDefault();
					e.stopPropagation();
					var input  = $(this);

					if(config.events.beforeUpdateComment(items, index, this) != true)
					{
						$(this).val(items[index].description);
						return;
					}

					$('body').addLoader();

					$.ajax({
						data     : {id : model.id,  [config.inputComment.name]: input.val() },
						method   : 'POST',
						dataType : 'JSON',
						url      : config.routes.update,
					})

					.always(function(){
						$('body').rmLoader();
					})
					.done(function(data){

						if(data.status != true)
						{
							$(input).val(items[index].description);
							config.events.afterUpdateComment(data);
							return;
						}

						items[index].description = data.model.description;
						config.events.afterUpdateComment(data);
					})
					.fail(function(data){
						config.events.errorOnUpdateComment(data);
					})
				});
		}

		function renderBoxAdd(append){

			if($(el).find(".main-box-gallery .gallery-icon-photos").length > 0)
				return;

			append = isBoolean(append) ? true : false;

			boxAdd.addClass('main-box-gallery');
			if(append == true)
				boxAdd.appendTo(el);
			else
				boxAdd.prependTo(el);

			var btnAdd = $('<div>');
				btnAdd.addClass('box-add-item')
				.html('<div><div class="icon gallery-icon-photos"></div><div><span>'+ config.labels.addItem +'</span></div></div>')
				.appendTo(boxAdd);

			//@todo add event drop
			btnAdd.on('click', function(e){
				e.preventDefault();
				e.stopPropagation();
				inputFile.click();
			});
        }
        function loadData(callback){
			el.empty().addLoader();
			dGrid.empty();

			var jqxhr = $.getJSON(config.routes.list, function(data){
				items = data;
			})
			.done(function() {
				var _callback = function(){
					renderGrid();

					inputFile.off();
					inputFile.on('change', function(e){
						var files = e.target.files;
						var aval  = (function(){
							if(items.length > config.inputFile.maxFiles)
								return 0;
							else
								return (config.inputFile.maxFiles  - items.length);
						})();
						if(aval == 0)
						{
							$(boxAdd).fadeOut().remove();
							boxAdd = $('<div>');
							config.events.onMaxImages();
							return;
						}

						$(files).each(function(k,v){

							if(aval == 0)
							{
								$(boxAdd).fadeOut().remove();
								boxAdd = $('<div>');
								config.events.onMaxImages();
								return false;
							}

							//@todo validaciones aqui:
							//@todo validacon minmo tamaño (v.size);
							//@todo validacon minimo with ; minimo height (v.width || v.height);
							//@todo maximo with ; maximo height (v.width || v.height);

							if((/\.(png|jpeg|jpg)$/i).test(v.name) == false)
								return;

							var img = new Image();
							img.addEventListener("load", function () {
								upload(v, this.src);
							});

							img.src = URL.createObjectURL(e.target.files[k]);

							setTimeout(function(){
								 $(e.target).val("");
							}, 250);

							aval--;
						});

					});

					if( isFunction(callback))
						callback();
				};

				el.rmLoader(_callback);
			})
			.fail(function(data) {
				el.rmLoader(function(){
					config.events.errorOnLoad(data);
				})
			});
		}

		function upload(file, src){
			var imgCached       = src;
			var jqxhr    		= null;
			var parent   		= $(boxAdd);
			var idNode	        = uniqid();
			var idBtnCancel		= uniqid();
			var idProgressBar  	= uniqid();
			var idProgressText 	= uniqid();
			var name            = file.name;

			function abort(){
				if(jqxhr != null)
					jqxhr.abort();

				$("#"+idNode).fadeOut("fast",function(){
					$(this).remove();
				});
			}

			function progressHandling(event){
				var position = event.loaded || event.position;
				var total    = event.total;

				if (event.lengthComputable)
				{
					var progress = Math.ceil(position / total * 100);
					setTimeout(function(){

						if(progress > 99)
						{
							$("#"+idBtnCancel).fadeOut("fast", function(){
								$(this).remove();
							});
						}

						console.log(progress + "% file " + name);
						$("#" + idProgressText).text(progress);
						$("#" + idProgressBar).css("width", progress + "%");

					}, 200);
				}
            }
            function send(){
				var formData = new FormData();
					formData.append([config.inputFile.name], file , [config.inputFile.name]);

				var myXhr = null;

				$.ajax({
					type          : 'POST',
					url           : config.routes.create,
					async         : true,
					data          : formData,
					cache         : false,
					contentType   : false,
					processData   : false,
					timeout       : 2*60*60*1000,

					xhr: function () {
						myXhr = $.ajaxSettings.xhr();
						if (myXhr.upload)
							myXhr.upload.addEventListener('progress', progressHandling, false);
						return myXhr;
					}
				})
				.fail(function(data){
					/// @todo add error report
					$("#" + idNode).fadeOut();
					config.events.errorOnUploadImage(data);
				})
				.done(function(data){
					if(data.status == true)
					{
						data.model.url = {
							thumnails : imgCached ,
							large     : imgCached ,
						};

						items.push(data.model);
						renderItem(data.model, (items.length - 1) );
						$("#" + idNode).fadeOut();
					}
					else{
						///@todo add Exception not save
						//window.location.reload(true);
						$("#" + idNode).fadeOut();
						config.events.afterUploadImage(data);
					}
				});


				jqxhr = myXhr;
			}

			(function(){
				html = "";
				html+="<div id=\""+ idNode +"\" class=\"item\">";
				html+="<div style=\"z-index: 0;position:absolute;width:100%;height:100%;background-image: url(\'"+imgCached+"\');background-repeat: no-repeat;background-position: center center;background-size: cover;opacity: 0.7;\"></div>";
				html+="<div style=\"position:absolute;z-index:1;left:0;right:0;top:0;bottom:0;background-color:rgba(0,0,0, 0.7);\">";
				html+="<div class=\"clearfix\">";
				html+="<div class=\"pull-right padding-15\">";
				html+="<i id=\""+ idBtnCancel+"\"  class=\"fa fa-2x fa-times-circle\" style=\"color:#FFF;cursor:pointer; background: #008CBA;padding-top:2px;;border-radius:50%;padding-left:3px; padding-right:3px\"></i>";
				html+="</div>";
				html+="</div>";
				html+="";
				html+="<div style=\"position:absolute;left:0;right:0;bottom:0; margin:15px\">";
				html+="<div style=\"background:#DFDFDF;height:15px;border:1px solid #008CBA; padding:2px; border-radius:4px; overflow: hidden;\">";
				html+="<div  id=\""+ idProgressBar+"\"  style=\"background:#008CBA; height:100%; border-radius:4px; width:0%;\"></div>";
				html+="</div>";
				html+="<div class=\"text-right\" style=\"font-weight:bold; padding-top:5px; color:#FFF\">";
				html+="<span id=\""+ idProgressText +"\" >0</span>%";
				html+="</div>";
				html+="</div>";
				html+="</div>";
				html+="</div>";
				parent.append(html);
				// events;
				$("#"+idBtnCancel).on("click", function(e){
					e.preventDefault();
					e.stopPropagation();
					abort();
				});

				//sendAjax
				send();
			})();
		}

		function previewModal(index)
		{
			modal.addLoader();

			var data = items[index] || null;

			if(data === null)
			{
				modal.reset('events');
				modal.close();
				loadData();
				return;
			}

			// generate picture
			var pic = (function(){
				var obj = $('<div>');
				obj.css({
					'background-image'    	: 'url('+  data.url.thumnails +')',
					'background-repeat'   	: 'no-repeat',
					'background-position' 	: 'center',
					'background-size'		: 'cover',
					'width'					: '100%',
					'height'                : '100%',
				});

				// render btn next | prev
				if(items.length > 1)
				{
					switch(true)
					{
						case (index == 0):
							var prevIndex = items.length-1;
							var nextIndex = index+1;
							break;

						case (index == (items.length-1) ):
							var prevIndex = index-1;
							var nextIndex = 0;
							break;

						default:
							var prevIndex = index-1;
							var nextIndex = index+1;
							break;
					}

					var btnPrev = $('<a>');
						btnPrev
						.addClass('gallery-icon-arrow-left gallery-icon-action')
						.css({
						    'position': 'absolute',
						    'left': '0px',
						    'margin-left': '-55px',
						    'top': '43%',
						})
						.on('click', function(){
							previewModal(prevIndex);
						}).appendTo(obj);

					var divComment = $('<div>');
						divComment
						.addClass('text-left')
						.text('');

					var btnNext = $('<a>')
						.css({
						    'position': 'absolute',
						    'left': '100%',
						    'top': '43%',
						    'margin-left': '27px'
						});
						btnNext.addClass('gallery-icon-arrow-right gallery-icon-action');
						btnNext.on('click', function(){
							previewModal(nextIndex);
						}).appendTo(obj);
				}

				return obj;
			})();
			// generate comment:
			var comment = (function(){
				var div = $('<div>');

				var p = $('<p>');
					p.addClass('gallery-item-comment')
					.text(data.description)
					.appendTo(div);

				return div;
			})();

			// generate btn delete items
			var btnDelete = (function(){
				var obj = $('<button>');
					obj
					.addClass('btn text-right btn-danger')
					.text(config.labels.rmItem)
					.on('click', function(){

						if(config.events.beforeDelete(items, index, pic) != true)
							return false;

						modal.confirm({
							labelCancel    : config.labels.confirm.cancel,
							labelOK        : config.labels.confirm.continue,
							title          : config.labels.confirm.title,
							confirm        : config.labels.confirm.msn,
							callbackOk     : function(){

								$('body').addLoader();

								$.ajax({
									data     : {id : data.id },
									method   : 'POST',
									dataType : 'JSON',
									url      : config.routes.delete,
								})
								.always(function(){
									$('body').rmLoader();
								})
								.done(function(data){

									if(data.status == true)
									{

										$($(el).find(".main-box-gallery .item").get(index)).fadeOut('fast', function(){
											$(this).remove();
										});

										items.splice(index, 1);
										if(items.length < config.inputFile.maxFiles )
											renderBoxAdd(true);

										if(items.count == 1)
											modal.close();
										else{
											$newIndex = (index-1 < 0)? 0 : index-1;
											previewModal($newIndex);
										}
									}

									config.events.afterDelete(data);
								})
								.fail(function(data){
									config.events.errorOnDelete(data);
								})
							}
						});
					});
				return obj;
			})();

			modal.reset.default(true);
			modal.icon.attr("class", "gallery-icon-photo");
			modal.size('modal-lg');
			modal.title.html( function(){
				var html = '<span>'+ config.title + ' ' + (index+1) + '/' + items.length + '</span> <div class="pull-right" style="margin-right:15px;font-size:12px;line-height:20px	">'+ data.created_at+'</div>';
				return html;

			}).css('margin-left', '15px');

			modal.header.show();
			modal.body.addClass('gallery-picture-content');

			modal.footer
				.append(comment)
			    .append(btnDelete)
			    .show();

			modal.rmLoader( function(){
				modal.body.html(pic);
			});
		}

		function renderGrid(){

			if(items.length < config.inputFile.maxFiles )
				renderBoxAdd();

			dGrid.addClass('main-box-gallery');
			dGrid.prependTo(el);

			$(items).each(function(k,v){
				renderItem(v, k);
			});

			if(isFunction(config.events.afterRender))
				config.events.afterRender();
		}

		loadData();
	};
})(jQuery);

