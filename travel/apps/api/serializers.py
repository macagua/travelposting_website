from typing import Any

from drf_writable_nested import WritableNestedModelSerializer
from html_json_forms.serializers import JSONFormSerializer
from rest_framework import serializers

from apps.destinations.models import (
    Destination,
    TourData,
    TabData,
    HeaderSection,
    DestinationDetail,
    GeneralDetail,
    InventarioDetail,
    BookingDetail,
    OptionTabData,
    Photo,
)


class OptionTabDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionTabData
        fields = '__all__'


class TabDataSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="option_tab.name", required=False)

    class Meta:
        model = TabData
        exclude = ('tour_data',)


class TourDataSerializer(JSONFormSerializer, WritableNestedModelSerializer):
    tab = TabDataSerializer(many=True, read_only=False)

    class Meta:
        model = TourData
        exclude = ('destination',)


class HeaderSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderSection
        exclude = ('destination',)


class GeneralDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralDetail
        exclude = ('destination_detail',)


class InventarioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioDetail
        exclude = ('destination_detail',)


class BookingDetailSerializer(serializers.ModelSerializer):
    days = serializers.ListField(child=serializers.IntegerField(max_value=6, min_value=0))

    class Meta:
        model = BookingDetail
        exclude = ('destination_detail',)


class DestinationDetailSerializer(JSONFormSerializer, WritableNestedModelSerializer):
    general = GeneralDetailSerializer(many=False, read_only=False)
    inventario = InventarioDetailSerializer(many=False, read_only=False)
    booking = BookingDetailSerializer(many=True, read_only=False)

    class Meta:
        model = DestinationDetail
        exclude = ('destination',)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('name', 'sort', 'description', 'image', 'thumbnail', 'created_at')

    def to_representation(self, instance: Any) -> Any:
        return {
            'id': instance.pk,
            'sort': instance.sort,
            'description': instance.description,
            'created_at': instance.created_at.strftime("%d/%m/%Y"),
            'url': {
                'thumnails': instance.thumbnail.url if instance.thumbnail else '',
                'large': instance.image.url if instance.image else ''
            }
        }


class PhotoWithDestinationSerializer(PhotoSerializer):
    class Meta(PhotoSerializer.Meta):
        fields = '__all__'


class DestinationSerializer(JSONFormSerializer, WritableNestedModelSerializer):
    tour = TourDataSerializer(many=False, read_only=False, required=False)
    header = HeaderSectionSerializer(many=False, read_only=False)
    details = DestinationDetailSerializer(many=False, read_only=False, required=False)
    gallery = PhotoSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Destination
        fields = '__all__'
        extra_kwargs = {'user': {'default': serializers.CurrentUserDefault()}}

def ItinerarySerializer(itinerary):
    mapped_object = []
    for count,data in enumerate(itinerary, start=1):
        dict_aux = {
            'fields': {
                'id': data.id,
                'counter': count,
                'destination': data,
                'short_title': data,
                'content': data,
            }
        }
        mapped_object.append(dict_aux)
    return json.dumps(mapped_object)
