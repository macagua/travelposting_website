from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from impersonate.admin import UserAdminImpersonateMixin
from apps.accounts.models import CustomerUser, Contact, Comment, LastVisitIP
from apps.utils.views import get_referal_code


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


def assing_referal_code(modeladmin, request, queryset):
    for user in queryset:
        user.ref_code=get_referal_code()
        user.save()
assing_referal_code.short_description = _("Assing refferal code")

@admin.register(CustomerUser)
class UserAdmin(UserAdminImpersonateMixin, BaseUserAdmin):
    """
        Class and Mixin creates to allow us to impersonate our users\
        that means that we are able to work with they, we can see exact\
        what they saw, so we can attend their requirements or understand their\
        problems; other use for this class is the normal crud for admin users.
    """

    actions = [assing_referal_code]

    # The forms to add and change user instances
    add_form = UserCreationForm
    open_new_window = True

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_joined', 'is_staff', 'is_active', 'password_link')
    list_filter = ('is_staff', 'is_active', ('last_login'), 'is_community')
    readonly_fields = ('subscription_id', 'last_ip', 'location')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'degree', 'last_ip', 'location', 'phone', 'mobile', 'language', 'facebook','instagram','twitter','linkedin', 'about_me')}),
        (_('Business info'), {'fields': ('business_name', 'business_address', 'business_position')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_community', 'subscription_id', 'groups','ref_code')}),
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


    def password_link(self, obj):
        from django.utils.html import mark_safe
        return mark_safe(f'<a href="/admin/accounts/customeruser/{obj.id}/password/">Change Password</a>')
    password_link.allow_tags = True
    password_link.short_description = 'password'


# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('user_from',)
    list_filter = ['user_from', ]
    list_display = [
        'user_from',
        'user_to',
        'created',
    ]


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('user_comment', 'user_answer',)
    list_filter = ['user_comment', 'user_answer']
    list_display = [
        'post',
        'user_comment',
        'created'
    ]


@admin.register(LastVisitIP)
class LastVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'location', 'last_ip_login')
    list_display = [
            'user',
            'location',
            'last_ip_login'
            ]
