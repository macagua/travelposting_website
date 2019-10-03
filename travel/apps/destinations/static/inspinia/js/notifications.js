function notification(type,msg){
	toastr[type](msg)
}


function notificationErrorFormLabels(data){
    var error_list="<ul>"
    $.each( data, function( key, value ) {
            $.each( value, function( label, error_form ){
                error_list+="<li><b>"+label + ":  " + error_form+"</b></li>";
            })
    });
    error_list=error_list+"</ul>"
    toastr['error'](error_list)
}



function notificationErrorForm(form_error){
    error_list="<ul>"
    $.each( form_error, function( key, value ) {
            error_list+="<li>"+key + ": " + value+"</li>";
    });
    error_list=error_list+"</ul>"

	toastr['error'](error_list)
}