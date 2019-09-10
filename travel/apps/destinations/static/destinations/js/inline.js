// Inicio TabData
function addTabData(event) {
    event.preventDefault();
    let numTabData = parseInt($("#id_tour-0-tabData-TOTAL_FORMS").val());
    let div = $('script[type="template/tab_data"]');
    $('#accordion').append(div.html());
    // div.html().replace(/__prefix__/g, numTabData);
    cambiarValores([numTabData]);
    $('#id_tour-0-tabData-' + numTabData + '-content').summernote();
    // crear funcion para agregar cualquier cosa al momento de cargar el nuevo formulario
    let total_forms = numTabData + 1;
    $("#id_tour-0-tabData-TOTAL_FORMS").val(total_forms);
}

function deleteTabData(event, t) {
    event.preventDefault();
    var numTabData = parseInt($("#id_tour-0-tabData-TOTAL_FORMS").val());
    $("#id_tour-0-tabData-TOTAL_FORMS").val(numTabData - 1);
    $(t).parent().parent().parent().remove();
}

// Fin TabData


// Inicio AddPeriod
function addPeriod(event) {
    const PREFIX = "id_details";
    const TOTAL = "TOTAL_FORMS";
    event.preventDefault();

    let forms = $("#"+ PREFIX + "-0-booking-" + TOTAL);
    // language=JQuery-CSS
    let div = $('script[type="template/booking"]');
    // language=JQuery-CSS
    $("#booking .border-bottom:last").after(div.html());
    // div.html().replace(/__prefix__/g, cant);
    cambiarValores([parseInt(forms.val())]);
    // crear funcion para agregar cualquier cosa al momento de cargar el nuevo formulario
    const fields = ["start_date", "end_date"];
    for (let i = 0; i < fields.length; i++) {
        let element = $("#"+ PREFIX +"-0-booking-" + forms.val() + "-" + fields[i]);
        let data = JSON.parse(element.attr('dp_config'));
        element.attr('dp_config');
        element.datetimepicker(data.options);
    }
    let total_forms = parseInt(forms.val()) + 1;
    forms.val(total_forms);
}

function deletePeriod(event, t) {
    const TOTAL = "TOTAL_FORMS";
    const PREFIX = "id_details";
    event.preventDefault();
    let forms = $("#" + PREFIX + "-0-booking-" + TOTAL);
    var numTabData = parseInt(forms.val());
    forms.val(numTabData - 1);
    $(t).parent().parent().parent().remove();
}

// Fin Period

function cambiarValores(array) {
    for (let j = 0; j < array.length; j++) {
        $('[name*="__prefix__"]').each(function (i, field) {
            let name = $(this).attr('name').replace('__prefix__', array[j]);
            $(this).attr('name', name);
        });
        $('[for*="__prefix__"]').each(function (i, label) {
            let name = $(this).attr('for').replace('__prefix__', array[j]);
            $(this).attr('for', name)
        });
        $('[onclick*="__prefix__"]').each(function (i, funct) {
            let name = $(this).attr('onclick').replace('__prefix__', array[j]);
            $(this).attr('onclick', name);
        });
        $('[class*="__prefix__"]').each(function (i, cls) {
            let name = $(this).attr('class').replace('__prefix__', array[j]);
            $(this).attr('class', name);
        });
        $('[type*="__prefix__"]').each(function (i, tp) {
            let name = $(this).attr('type').replace('__prefix__', array[j]);
            $(this).attr('type', name);
        });
        $('[href*="__prefix__"]').each(function (i, obj) {
            let name = $(this).attr('href').replace('__prefix__', array[j]);
            $(this).attr('href', name)
        });
        $('[src*="__prefix__"]').each(function (i, obj) {
            let name = $(this).attr('src').replace('__prefix__', array[j]);
            $(this).attr('src', name)
        });
        $('[id*="__prefix__"]').each(function (i, obj) {
            let name = $(this).attr('id').replace('__prefix__', array[j]);
            $(this).attr('id', name)
        });
    }
}