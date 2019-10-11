from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from impersonate.admin import UserAdminImpersonateMixin
from apps.accounts.models import CustomerUser


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = CustomerUser
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomerUser
        fields = ('email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_name', 'first_name',
                  'degree', 'phone', 'mobile', 'language', 'business_name', 'business_address', 'business_position')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


@admin.register(CustomerUser)
class UserAdmin(UserAdminImpersonateMixin, BaseUserAdmin):
    """
        Class and Mixin creates to allow us to impersonate our users\
        that means that we are able to work with they, we can see exact\
        what they saw, so we can attend their requirements or understand their\
        problems; other use for this class is the normal crud for admin users.
    """

    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    open_new_window = True

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_joined', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', ('last_login'))
    readonly_fields = ('subscription_id',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'degree', 'phone', 'mobile', 'language', 'facebook','instagram','twitter','linkedin')}),
        (_('Business info'), {'fields': ('business_name', 'business_address', 'business_position')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'subscription_id')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
