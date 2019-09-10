from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django_summernote.widgets import SummernoteInplaceWidget
from bootstrap_datepicker_plus import DatePickerInput
from oauth2_provider.models import Application

from tour.destinations.models import (
    TourData,
    HeaderSection,
    Destination,
    DestinationDetail,
    TabData, GeneralDetail,
    InventarioDetail,
    BookingDetail,
    Photo,
)
from tour.accounts.forms import BaseBootstrapForm
from tour.destinations.widgets import BootstrapMoneyWidget


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del tour')
            }),
            'short_description': SummernoteInplaceWidget(attrs={
                'summernote': {'width': '100%', 'height': '200px'}
            }),
            'description': SummernoteInplaceWidget(attrs={
                'summernote': {'width': '100%', 'height': '500px'}
            }),
            'user': forms.HiddenInput(attrs={
                'read_only': True
            })
        }

    class Media:
        css = {
            'all': (
                'destinations/css/style.css',
            )
        }


class TourDataForm(BaseBootstrapForm, forms.ModelForm):
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
    def has_changed(self):
        return super(TourDataInlineFormSet, self).has_changed()


class TabDataForm(forms.ModelForm):
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


TabDataFormSet = forms.inlineformset_factory(TourData, TabData, formset=TabDataInlineFormSet, form=TabDataForm, extra=1,
                                             min_num=0, max_num=10)


class HeaderSectionInlineForm(BaseBootstrapForm, forms.ModelForm):
    class Meta:
        model = HeaderSection
        fields = '__all__'


class DestinationDetailForm(BaseBootstrapForm, forms.ModelForm):
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
    class Meta:
        model = GeneralDetail
        fields = '__all__'
        widgets = {
            'regular_price': BootstrapMoneyWidget,
            'sale_price': BootstrapMoneyWidget,
            'date_on_sale_from': DatePickerInput(format='%Y-%m-%d'),
            'date_on_sale_to': DatePickerInput(format='%Y-%m-%d')
        }


GeneralDetailInlineFormSet = forms.inlineformset_factory(DestinationDetail, GeneralDetail, form=GeneralDetailForm,
                                                         extra=1, min_num=0, max_num=1)


class InventarioDetailForm(BaseBootstrapForm, forms.ModelForm):
    class Meta:
        model = InventarioDetail
        fields = '__all__'


InventarioDetailInlineFormSet = forms.inlineformset_factory(DestinationDetail, InventarioDetail,
                                                            form=InventarioDetailForm, extra=1, min_num=0, max_num=1)


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


BookingDetailInlineFormSet = forms.inlineformset_factory(DestinationDetail, BookingDetail, form=BookingDetailForm,
                                                         extra=0, min_num=1, max_num=10)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'sort', 'description', 'thumbnail', 'image')


class ApplicationForm(BaseBootstrapForm, forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'client_id', 'client_secret', 'client_type', 'authorization_grant_type', 'redirect_uris')
        labels = {
            'name': _("Nombre"),
            'authorization_grant_type': _("Tipo de aut."),
            'redirect_uris': _("Redirect uris")
        }
