from django import forms


class BaseBootstrapForm:
    def __init__(self, *args, **kwargs):
        super(BaseBootstrapForm, self).__init__(*args, **kwargs)

        for name, value in self.fields.items():
            if not isinstance(value.widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple)):
                value.widget.attrs.setdefault('class', 'form-control')
                value.widget.attrs.setdefault('placeholder', value.label)


class FieldKwargsMeta:
    def __init__(self, *args, **kwargs):
        super(FieldKwargsMeta, self).__init__(*args, **kwargs)

        if hasattr(self.Meta, 'fields_kwargs'):
            fields_kwargs = self.Meta.fields_kwargs.copy()

            for field, value in fields_kwargs.items():
                if 'queryset' in value.keys():
                    self.fields[field].queryset = value.pop('queryset')

                self.fields[field].__dict__.update(value)


class BaseModelForm(FieldKwargsMeta, forms.ModelForm):
    pass


class FullModelForm(BaseBootstrapForm, BaseModelForm):
    pass
