from django import forms

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from mapwidgets.widgets import GooglePointFieldWidget
from django_summernote.widgets import SummernoteInplaceWidget
from bootstrap_datepicker_plus import DatePickerInput,TimePickerInput
from apps.accounts.forms import BaseBootstrapForm
from apps.destinations.widgets import BootstrapMoneyWidget
from apps.destinations.models import (
    TourData,
    HeaderSection,
    Destination,
    DestinationDetail,
    TabData, GeneralDetail,
    InventarioDetail,
    BookingDetail,
    Photo,
    Itinerary,
    DestinationMap,
)


class DestinationForm(forms.ModelForm):
    """
        Form for save new destinations thru the frontend dashboard.
    """
    class Meta:
        model = Destination
        fields = [
            'user',
            'categorie',
            'name',
            'short_description',
            'description',
            'departure_date',
            'arrival_date',
            'departure_time',
            'arrival_time',
            'number_of_reservations',
            'transfer_from',
            'tour_include',
            'tour_not_include',
        ]

        widgets = {
            'user': forms.HiddenInput(attrs={
                'read_only': True
            }),

            'categorie': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': _('Category'),
                'style':'width:100%',
                'required':True,
            }),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del tour'),
                'required':True,

            }),

            'short_description': forms.Textarea(attrs ={
                'maxlength': 250,
                'class':'form-control',
                'required':True,
            }),

            'description': SummernoteInplaceWidget(attrs={
                'summernote': {'width': '100%', 'height': '250px'},
                'required':True,
            }),

            'departure_date': DatePickerInput(
                attrs ={
                    'required':True,
                },
                options={
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    "widgetPositioning": {
                        "horizontal":"auto",
                        "vertical":"bottom",
                    },
                }).start_of('event days'),

            'arrival_date': DatePickerInput(
                attrs ={
                    'required':True,
                },
                options={
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }).end_of('event days'),

            'departure_time':TimePickerInput(
                attrs ={
                    'required':True,
                },
                ).start_of('party time'),

            'arrival_time': TimePickerInput(
                attrs ={
                    'required':True,
                },
                ).end_of('party time'),

            'number_of_reservations': forms.NumberInput(),

            'transfer_from':forms.TextInput(),

            'tour_include':SummernoteInplaceWidget(attrs={
                'summernote': {'width': '100%', 'height': '250px'},
                'required':True,
            }),

            'tour_not_include':SummernoteInplaceWidget(attrs={
                'summernote': {'width': '100%', 'height': '250px'},
                'required':True,
            }),
        }

    class Media:
        css = {
            'all': (
                'destinations/css/style.css',
            )
        }


class TourDataForm(BaseBootstrapForm, forms.ModelForm):
    """
        ModelForm to save the correspondient data as a inline on destination create/update view.
    """
    def __init__(self, *args, **kwargs):
        super(TourDataForm, self).__init__(*args, **kwargs)

        prefix = f"{self.prefix}-tabData"
        self.tab_data_inlineformset = TabDataFormSet(instance=self.instance, data=self.data or None,
                                                     prefix=prefix)

    def is_valid(self):
        return super(TourDataForm, self).is_valid() and self.tab_data_inlineformset.is_valid()

    def save(self, commit=True):
        # assert commit == True  # Guardar manualmente en el view
        res = super(TourDataForm, self).save(commit=commit)
        res.save()
        self.tab_data_inlineformset.save()
        return res

    def has_changed(self):
        return super(TourDataForm, self).has_changed() or self.tab_data_inlineformset.has_changed()

    class Meta:
        model = TourData
        fields = '__all__'

    class Media:
        js = (
            'destinations/js/inline.js',

        )


class TourDataInlineFormSet(forms.BaseInlineFormSet):
    """
        Tab options on change inlineformset.
    """
    def has_changed(self):
        return super(TourDataInlineFormSet, self).has_changed()


class TabDataForm(forms.ModelForm):
    """
        Initial and Metas for ```TabData````Model.
    """
    def __init__(self, *args, **kwargs):
        super(TabDataForm, self).__init__(*args, **kwargs)

        if '__prefix__' in kwargs.get('prefix', '').split('-'):
            self.fields['content'].widget = forms.Textarea()

    class Meta:
        model = TabData
        fields = '__all__'
        widgets = {
            'content': SummernoteInplaceWidget(attrs={
                'summernote': {'width': '100%', 'height': '200px'}
            }),
            'option_tab': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': _('Option'),
                'onchange': 'ajaxView(this, "GET")',
                'data-get-template-url': reverse_lazy('destinations:option-template', kwargs={'pk': 0})
            })
        }

    class Media:
        js = (
            'destinations/js/ajax-view.js',
        )


class TabDataInlineFormSet(forms.BaseInlineFormSet):
    """
        Base for clean and validate the tabs for formtabs in dashboard destination app.
    """
    def clean(self):
        super(TabDataInlineFormSet, self).clean()
        options_tab = []

        for form in self.forms:
            option_tab = form.cleaned_data.get('option_tab')

            if option_tab in options_tab:
                raise forms.ValidationError(_(
                    "El tab '%(tab)s' se encuentra duplicado, debe estar una sola vez."), code="duplicated",
                    params={'tab': option_tab})
            options_tab.append(option_tab)

#Setting the inline.
TabDataFormSet = forms.inlineformset_factory(
    TourData,
    TabData,
    formset=TabDataInlineFormSet,
    form=TabDataForm,
    extra=1,
    min_num=0, max_num=10,
)


class HeaderSectionInlineForm(BaseBootstrapForm, forms.ModelForm):
    """
        ModelForm to the ```Header``` model in to dashboard.
        @TODO: consider if can be deleted.
    """
    class Meta:
        model = HeaderSection
        fields = '__all__'


class DestinationDetailForm(BaseBootstrapForm, forms.ModelForm):
    """
        ModelForm used for save the data about all destiantion's details.
    """



    def __init__(self, *args, **kwargs):
        super(DestinationDetailForm, self).__init__(*args, **kwargs)

        prefix = f'{self.prefix}-%(name)s'
        self.general_inlineformset = GeneralDetailInlineFormSet(instance=self.instance, data=self.data or None,
                                                                prefix=prefix % {'name': 'general'})
        self.inventario_inlineformset = InventarioDetailInlineFormSet(instance=self.instance, data=self.data or None,
                                                                      prefix=prefix % {'name': 'inventario'})
        self.booking_inlineformset = BookingDetailInlineFormSet(instance=self.instance, data=self.data or None,
                                                                prefix=prefix % {'name': 'booking'})

    def is_valid(self):
        return super(DestinationDetailForm, self).is_valid() and self.general_inlineformset.is_valid() and \
               self.inventario_inlineformset.is_valid() and self.booking_inlineformset.is_valid()

    def save(self, commit=True):
        # assert commit == True  # Guardar a manualmente en el view
        res = super(DestinationDetailForm, self).save(commit=commit)
        res.save()
        self.general_inlineformset.save()
        self.inventario_inlineformset.save()
        self.booking_inlineformset.save()
        return res

    def has_changed(self):
        changes_inlines = [
            super(DestinationDetailForm, self).has_changed(),
            self.general_inlineformset.has_changed(),
            self.inventario_inlineformset.has_changed(),
            self.booking_inlineformset.has_changed()
        ]
        return any(changes_inlines)

    class Meta:
        model = DestinationDetail
        fields = '__all__'


class GeneralDetailForm(BaseBootstrapForm, forms.ModelForm):
    """
        `GeneralDetail` class to show widget for this form.
    """
    class Meta:
        model = GeneralDetail
        fields = '__all__'
        widgets = {
            'regular_price': BootstrapMoneyWidget(
                attrs={
                'required':True,
                'class':'form-control money'
                }
            ),
            'sale_price': BootstrapMoneyWidget(attrs={
                'required':True,
                'class':'form-control money'
                }),
            'date_on_sale_from': DatePickerInput(format='%Y-%m-%d'),
            'date_on_sale_to': DatePickerInput(
                format='%Y-%m-%d',
                attrs ={
                    'required':True,

                },
                options={
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    "widgetPositioning": {
                        "horizontal":"auto",
                        "vertical":"bottom",
                    },
                }
            )
        }

#Setting the inline.
GeneralDetailInlineFormSet = forms.inlineformset_factory(
    DestinationDetail,
    GeneralDetail,
    form=GeneralDetailForm,
    extra=1,
    min_num=0,
    max_num=1,
)


class InventarioDetailForm(BaseBootstrapForm, forms.ModelForm):
    class Meta:
        model = InventarioDetail
        fields = '__all__'

    quantity = forms.IntegerField(
        required= True,
        initial=0,
        min_value=1,
        widget= forms.NumberInput(
            attrs={
                'class': 'form-control',
                'required':True,
            }
        )
    )

    umb_exist = forms.IntegerField(
        required= True,
        initial=0,
        min_value=1,
        widget= forms.NumberInput(
            attrs={
                'class': 'form-control',
                'required':True,
            }
        )
    )

    sold_individually = forms.BooleanField(
        initial=False,
        required=True
    )


#Setting the inline.
InventarioDetailInlineFormSet = forms.inlineformset_factory(
    DestinationDetail,
    InventarioDetail,
    form=InventarioDetailForm,
    extra=1,
    min_num=0,
    max_num=1,
)


class BookingDetailForm(BaseBootstrapForm, forms.ModelForm):
    class Meta:
        model = BookingDetail
        fields = '__all__'
        widgets = {
            'special_price': BootstrapMoneyWidget,
            'start_date': DatePickerInput(format="%Y-%m-%d"),
            'end_date': DatePickerInput(format="%Y-%m-%d"),
            'days': forms.CheckboxSelectMultiple(attrs={
                'class': 'list-unstyled list-inline'
            })
        }

#Setting the inline.
BookingDetailInlineFormSet = forms.inlineformset_factory(
    DestinationDetail,
    BookingDetail,
    form=BookingDetailForm,
    extra=0,
    min_num=1,
    max_num=10,
)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'sort', 'description', 'thumbnail', 'image')


class ItineraryForm(forms.ModelForm):
    """
        Form for itinerary
    """
    class Meta:
        model = Itinerary
        fields = [
            'destination',
            'short_description',
            'detail_itinerary',

        ]

        widgets = {
            'short_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Short description'),
                }
            ),

            'detail_itinerary': SummernoteInplaceWidget(attrs={
                'summernote': {'width': '100%', 'height': '200px'}
            }),
        }


class DestinationMapForm(forms.ModelForm):
    """
    Modelo para manejar los mapas de google
    usados en los tours(destinos)
    """
    class Meta:
        model= DestinationMap
        fields = {
            'destination',
            'description_map',
            'map_destinie'

        }

        widgets = {
            'map_destinie': GooglePointFieldWidget,
            'description_map': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Description for map'),
                },
            )
        }
