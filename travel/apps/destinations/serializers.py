import json

def ItinerarySerializer(itinerary):
    mapped_object = []
    for count,data in enumerate(itinerary, start=1):
        dict_aux = {
            'fields': {
                'id': data.id,
                'counter': count,
                'destination': data.destination.name,
                'short_title': data.short_description,
                'content': data.detail_itinerary,
            }
        }
        mapped_object.append(dict_aux)
    return mapped_object

def DestinySerializer(destination):
    mapped_object = []
    for data in destination:
        dict_aux = {
                'id': data.id,
                'text': data.name,
        }
        mapped_object.append(dict_aux)
    return mapped_object

def mapped_errors_form(form):
    mapped_object = []
    for field_form in form:
        for error_form in field_form.errors:
            mapped_object.append({ str(field_form.label):[error_form]})
    return mapped_object