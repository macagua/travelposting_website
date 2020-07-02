from django.db import models
from djmoney.money import Money
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _


class Coupon(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100,
    )

    code = models.SlugField(
        _('code'),
        unique=True,
    )

    plan = models.ForeignKey(
        'landing_page.Plan',
        on_delete=models.CASCADE,
        related_name='coupons',
        verbose_name=_('plan'),
    )

    price = MoneyField(
        _('Price'),
        max_digits=8,
        decimal_places=2,
        default_currency='USD',
        default=Money(0, 'USD'),
        null=True,
        blank=True,
    )

    description = models.TextField(
        _('description'),
        blank=True,
        null=True,
    )

    start_date = models.DateTimeField(
        _('start date'),
    )

    end_date = models.DateTimeField(
        _('end date'),
    )

    quantity = models.PositiveIntegerField(
        _('quantity'),
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('end_date', 'start_date')
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')

    def __str__(self):
        return self.name
