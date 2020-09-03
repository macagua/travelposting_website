from django import forms
from apps.advertisements.models import (
    Advertiser,
    Category,
    Ad,
    AdImage,
    # Impression,
    # Click
)


class AdvertiserCreateForm(forms.ModelForm):
    class Meta:
        model = Advertiser
        fields = '__all__'


class AdvertiserUpdateForm(forms.ModelForm):
    class Meta:
        model = Advertiser
        fields = '__all__'


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AdCreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('title', 'url', 'publication_date', 'publication_date_end', 'advertiser', 'category', 'zone', 'weight', 'created_by')


class AdUpdateForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('title', 'url', 'publication_date', 'publication_date_end', 'advertiser', 'category', 'zone', 'weight', 'created_by')


class AdImageCreateForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = '__all__'


class AdImageUpdateForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = '__all__'
