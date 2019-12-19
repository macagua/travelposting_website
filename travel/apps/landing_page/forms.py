from django import forms
from apps.landing_page.models import ContactUs
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

    email = forms.EmailField(
    )

    message = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg date',
            },
        ),
    )

    ip_client = forms.GenericIPAddressField()

    captcha = ReCaptchaField(
	    widget=ReCaptchaV2Checkbox(
	        attrs={
	            'required_score':0.5,
	        }
	    )
    )