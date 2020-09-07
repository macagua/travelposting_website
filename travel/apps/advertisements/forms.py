from django import forms
from django.utils.translation import gettext_lazy as _
from bootstrap_datepicker_plus import DateTimePickerInput
from apps.advertisements.models import (
    Advertiser,
    Category,
    Ad,
    AdImage,
)


class AdvertiserCreateForm(forms.ModelForm):
    class Meta:
        model = Advertiser
        fields = '__all__'

        widgets = {
            'company_name': forms.TextInput(
                attrs={'class': 'form-control',},
            ),
            'website': forms.URLInput(
                attrs={'class': 'form-control',},
            ),
            'created_by': forms.Select(
                attrs={'class': 'form-control',},
            ),
        }


class AdvertiserUpdateForm(forms.ModelForm):
    class Meta:
        model = Advertiser
        fields = '__all__'

        widgets = {
            'company_name': forms.TextInput(
                attrs={'class': 'form-control',},
            ),
            'website': forms.URLInput(
                attrs={'class': 'form-control',},
            ),
            'created_by': forms.Select(
                attrs={'class': 'form-control',},
            ),
        }


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',},
            ),
            'description': forms.TextInput(
                attrs={'class': 'form-control',},
            ),
            'created_by': forms.Select(
                attrs={'class': 'form-control',},
            ),
        }


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',},
            ),
            'description': forms.TextInput(
                attrs={'class': 'form-control',},
            ),
            'created_by': forms.Select(
                attrs={'class': 'form-control',},
            ),
        }


ADS_ZONES = (
    ('', u'--------'),
#     (1, _('Header')),
#     (2, _('Content')),
    (3, _('Sidebar'))
)


class AdCreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            'title',
            'url',
            'publication_date',
            'publication_date_end',
            'advertiser',
            'category',
            'zone',
            'weight',
            'created_by'
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',},
            ),
            'url': forms.URLInput(
                attrs={'class': 'form-control',},
            ),
            'publication_date': DateTimePickerInput(
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
            ).start_of('event days'),
            'publication_date_end': DateTimePickerInput(
                attrs ={
                    'required':True,
                },
                options={
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
            ).end_of('event days'),
            'category': forms.Select(
                attrs={'class': 'form-control',},
            ),
            'zone': forms.Select(attrs={
                'class': 'selectpicker form-control',
                },
                choices = ADS_ZONES,
            ),
        }


class AdUpdateForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            'title',
            'url',
            'publication_date',
            'publication_date_end',
            'advertiser',
            'category',
            'zone',
            'weight',
            'created_by'
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',},
            ),
            'url': forms.URLInput(
                attrs={'class': 'form-control',},
            ),
            'publication_date': DateTimePickerInput(
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
            ).start_of('event days'),
            'publication_date_end': DateTimePickerInput(
                attrs ={
                    'required':True,
                },
                options={
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
            ).end_of('event days'),
            'advertiser': forms.Select(
                attrs={'class': 'form-control',},
            ),
            'category': forms.Select(
                attrs={'class': 'form-control',},
            ),
            'zone': forms.Select(attrs={
                'class': 'form-control',
                },
                choices = ADS_ZONES,
            ),
        }


class AdImageCreateForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = '__all__'

        widgets = {
            'ad': forms.Select(
                attrs={'class': 'form-control',},
            ),
            'device': forms.Select(
                attrs={'class': 'form-control',},
            ),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control',},
            ),
        }


class AdImageUpdateForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = '__all__'

        widgets = {
            'ad': forms.Select(
                attrs={'class': 'form-control',},
            ),
            'device': forms.Select(
                attrs={'class': 'form-control',},
            ),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control',},
            ),
        }
