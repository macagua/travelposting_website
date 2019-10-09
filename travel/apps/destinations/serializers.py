import json
from django.utils.html import mark_safe, escapejs

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

def MapSerializer(maps):
    mapped_object = []
    for count,data in enumerate(maps, start=1):
        dict_aux = {
            'fields': {
                'id': data.id,
                'counter': count,
                'destination': data.destination.name,
                'description': data.description_map,
                'map': escapejs(data.map_destinie),
            }
        }
        mapped_object.append(dict_aux)
    return mapped_object

def ItineraryAloneSerializer(itinerary):
    mapped_object = {
        'pk': itinerary.id,
        'destination': itinerary.destination.name,
        'destination_pk':itinerary.destination.id,
        'short_title': itinerary.short_description,
        'content': itinerary.detail_itinerary,

    }
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
