import logging

from django.core import validators, exceptions
from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _


logging.getLogger(__name__)


def parse_days_list(days: str, separator: str) -> list:
    days = days.split(f'{separator}')
    days_int = []

    for day in days:
        new_day = int(day)

        if not (0 <= new_day < 7):
            raise ValidationError(_("'%(day)s' is a day invalid"), code='invalid_day', params={'day': day})
        days_int.append(new_day)
    return days_int


DAYS_CHOICES = (
    (0, _('Sunday')), (1, _('Monday')), (2, _('Tuesday')), (3, _('Wednesday')),
    (4, _('Thursday')), (5, _('Friday')), (6, _('Saturday'))
)


class DaysCommaField(models.CharField):
    """Implements days with separator storage of lists"""

    # default_validators = [validators.validate_comma_separated_integer_list]
    description = _("String for storage days of lists")

    def __init__(self, separator: str = ",", *args, **kwargs) -> None:
        self.separator = separator
        kwargs.setdefault('max_length', 14)
        kwargs.setdefault('choices', DAYS_CHOICES)
        super(DaysCommaField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(DaysCommaField, self).deconstruct()

        if self.separator != ",":
            kwargs['separator'] = self.separator
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return value
        #return parse_days_list(value, self.separator)

    def to_python(self, value: (list, tuple, int, str)) -> list:
        if isinstance(value, (list, tuple, int)):
            return value

        if isinstance(value, str):
            if len(value.split(',')) == 1:
                return int(value)

        if value is None:
            return value

        return parse_days_list(value, self.separator)

    def validate(self, value: list, model_instance):
        for val in value:
            super(DaysCommaField, self).validate(val, model_instance)

    def get_prep_value(self, value: list):
        return f'{self.separator}'

    def formfield(self, **kwargs):
        defaults = {
            'choices_form_class': forms.TypedMultipleChoiceField
        }
        defaults.update(kwargs)
        return super(DaysCommaField, self).formfield(**defaults)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)
