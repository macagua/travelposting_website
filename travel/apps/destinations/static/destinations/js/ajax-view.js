function ajaxView(t, method) {
    let element = $(t);
    let tab = $(t).closest('.panel-collapse');

    $.ajax({
        url: element.attr('data-get-template-url').replace("0", element.val()),
        method: method,
        // data: form.serialize(),
        dataType: 'json',
        contentType: 'application/json; charset=UTF-8;',
        success: function (data, textStatus, jqXHR) {
            let content = tab.find('[name$="content"]');
            content.summernote('code', data.object.template);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    })
}