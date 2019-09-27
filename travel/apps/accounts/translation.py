from modeltranslation.translator import (
    register,
    TranslationOptions,
)

from apps.accounts.models import (
    CustomerUser,
)

@register(CustomerUser)
class CustomerUserTranslationOptions(TranslationOptions):
    fields = ('comment','business_position',)
