from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from easy_thumbnails.fields import ThumbnailerImageField

from apps.accounts.models import CustomerUser
from apps.destinations.fields import DaysCommaField
from cms.models import CMSPlugin



TEMPLATE_DESCRIPTION = """
<strong>Ingrese su título aquí...</strong><br><br>

<p> <b>Ingrese aquí su texto...</b></p>

<!--more--><br><br>

<p> <b>Ingrese más información aquí...</b></p>

<!--more--><br><br>

<strong>Quienes somos</strong><br><br>

<p><b>Por favor ingrese aquí su texto...</b></p><br><br>

<strong>Misión</strong><br><br>

<p><b>Por favor ingrese aquí su texto...</b></p><br><br>

<table class="table table-bordered tours-tabs__table" style="width: 100%px;">
<tbody>
<tr>
 <td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>
 <td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>
 <td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>
 <td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>
 <td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>
 <td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>INCLUIDO [icon_tick state="on"] </strong></td>
 <td style="width: 574.233px;">
  <b>Ingrese aquí lo que va incluido en el paquete como una lista...</b>
  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>
 </td>
</tr>
<tr>
 <td style="width: 213px;"><strong>NO INCLUIDO [icon_tick state="off"] </strong></td>
 <td style="width: 574.233px;">
  <b>Ingrese aquí lo que no va incluido en el paquete como una lista...</b>
  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>
 </td>
</tr>
</tbody>
</table>
"""

"""
class Categorie(models.Model):
    name = models.CharField(
        _('name'),
        max_length=50,
    )

    short_description= models.CharField(
        _('Short Description'),
        max_length=50,
    )

    image =  models.ImageField(
        _('Image'),
        upload_to="gallery/categorie/",
    )
"""
class Destination(models.Model):
    """
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        verbose_name=_("Categorie"),
    )
    """

    user = models.ForeignKey(
        CustomerUser,
        on_delete=models.CASCADE,
        verbose_name=_("Usuario"),
    )

    name = models.CharField(
        _('name'),
        max_length=200,
        blank=True,
        null=True,
    )

    short_description = models.TextField(
        _('Short description'),
        blank=True,
        null=True,
    )

    description = models.TextField(
        _('description'),
        blank=True,
        null=True,
        default=TEMPLATE_DESCRIPTION,
    )

    is_deleted = models.BooleanField(
        _('is_deleted'),
        default=False,
        editable=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("Destino")
        verbose_name_plural = _("Destinos")
        ordering = ('user',)

    def get_sku(self):
        return f"{self.details.inventario.sku}".upper()

    get_sku.short_description = _('SKU')

    @property
    def first_pic(self):
        pic = ''
        try:
            pic = Photo.objects.filter(destination=self).first()
            pic = pic.image.url
        except:
            pass
        return pic



class Photo(models.Model):
    destination = models.ForeignKey(
        Destination,
        related_name='gallery',
        on_delete=models.CASCADE,
        verbose_name=_('Destino'),
    )

    name = models.CharField(
        _('Nombre'),
        max_length=50,
        blank=True,
        null=True,
    )

    sort = models.IntegerField(
        _('Sort'),
        blank=True,
        null=True,
    )

    description = models.TextField(
        _('Descripción'),
        blank=True,
        null=True,
        default=_("Sin comentario"),
    )

    thumbnail = ThumbnailerImageField(
        _('Thumbnail'),
        upload_to="gallery/thumbnail/",
        blank=True,
        null=True,
    )

    image = models.ImageField(
        _('Imagen'),
        upload_to="gallery/image/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('sort', 'name')
        verbose_name = _('Foto')
        verbose_name_plural = _('Fotos')


class Badge(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=50,
    )

    description = models.TextField(
        _('Description'),
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = _('Badge')
        verbose_name = _('Badges')


class TourData(models.Model):
    destination = models.OneToOneField(
        Destination,
        related_name='tour',
        on_delete=models.CASCADE,
        verbose_name=_('Destino'),
    )

    badge = models.CharField(
        _('Badge'),
        max_length=150,
        blank=True,
        null=True,
        choices=(
            ('1', _('Ultimo minuto')),
            ('2', _('Deal del Mes')),
            ('3', _('FamTrip')),
            ('4', _('Congresos')),
            ('5', _('Eventos')),
            ('6', _('Hotel')),
            ('7', _('Movilidad')),
            ('8', _('Ocio +')),
        ),
    )

    def __str__(self):
        return f'{self.destination}'

    class Meta:
        verbose_name = _('Tour')
        verbose_name_plural = _('Tours')


class TabData(models.Model):
    tour_data = models.ForeignKey(
        TourData,
        related_name='tab',
        on_delete=models.CASCADE,
        verbose_name=_('Tour'),
    )

    option_tab = models.ForeignKey(
        'OptionTabData',
        related_name='option_tab',
        on_delete=models.CASCADE,
        verbose_name=_('Option tab'),
    )

    content = models.TextField(
        _('Content'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.option_tab}'

    class Meta:
        ordering = ('option_tab',)
        verbose_name_plural = _('Tabs')
        verbose_name = _('Tab')


class OptionTabData(models.Model):
    name = models.CharField(
        _('Nombre'),
        max_length=150,
    )

    description = models.TextField(
        _('Descripción'),
        blank=True,
        null=True,
    )

    template = models.TextField(
        _('Plantilla'),
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name',)
        verbose_name_plural = _('Opciones de las tabs')
        verbose_name = _('Opción de la tab')


class HeaderSection(models.Model):
    destination = models.OneToOneField(
        Destination,
        related_name='header',
        on_delete=models.CASCADE,
        verbose_name=_('Destino'),
    )

    display_mode = models.CharField(
        _('Display mode'),
        max_length=15,
        default='hide',
        choices=(
            ('hide', _('Default')),
            ('banner', _('Imagen')),
            ('slider', _('Slider')),
            ('from_list', _('From list'))
        ),
    )

    subtitle = models.CharField(
        _('Subtitle'),
        max_length=100,
        blank=True,
        null=True,
    )

    image = models.ImageField(
        _('Imagen'),
        upload_to='header/images',
        blank=True,
        null=True,
    )

    parallax = models.BooleanField(
        _('Parallax'),
        default=True,
    )

    image_repeat = models.CharField(
        _('Imagen repeat'),
        max_length=150,
        blank=True,
        null=True,
        choices=(
            ('repeat', _('Repeat')),
            ('no-repeat', _('No repeat')),
            ('repeat-x', _('Repeat horizontally')),
            ('repeat-y', _('Repeat vertically'))
        ),
    )

    mask = models.CharField(
        _('Mask'),
        max_length=120,
        blank=True,
        null=True,
        choices=(
            ('default', _('Default')),
        ),
    )

    def __str__(self):
        return f"{self.subtitle}"

    class Meta:
        verbose_name_plural = _('Secciones del encabezado')
        verbose_name = _('Sección del encabezado')


class DestinationDetail(models.Model):
    destination = models.OneToOneField(
        Destination,
        related_name='details',
        on_delete=models.CASCADE,
        verbose_name=_('Destino'),
    )

    var = models.BooleanField(
        _('Variable tour'),
        default=False,
    )

    virtual = models.BooleanField(
        _('Virtual'),
        default=False,
    )

    descargable = models.BooleanField(
        _('Descargable'),
        default=False,
    )

    def __str__(self):
        return f"{self.destination}-details"

    class Meta:
        verbose_name_plural = _('Detalles del destino')
        verbose_name = _('Detalle del destino')


class GeneralDetail(models.Model):
    destination_detail = models.OneToOneField(
        DestinationDetail,
        related_name='general',
        on_delete=models.CASCADE,
        verbose_name=_('Detalle del destino'),
    )

    regular_price = MoneyField(
        _('Precio normal'),
        max_digits=19,
        decimal_places=2,
        default_currency='USD',
        default=Money(0, 'USD'),
    )

    sale_price = MoneyField(
        _('Precio rebajado'),
        max_digits=19,
        decimal_places=4,
        default_currency='USD',
        default=Money(0, 'USD'),
    )

    date_on_sale_from = models.DateField(
        _('Fecha de rebaja inicial'),
        blank=True,
        null=True,
    )

    date_on_sale_to = models.DateField(
        _('Fecha de rebaja final'),
        blank=True,
        null=True,
    )

    status_imp = models.CharField(
        _('Estado del impuesto'),
        max_length=50,
        default='imponible',
        choices=(
            ('imponible', _('Imponible')),
            ('envio', _('Envio solamente')),
            ('ninguno', _('Ninguno'))
        ),
    )

    class_imp = models.CharField(
        _('Clase de impuesto'),
        max_length=50,
        default='estandar',
        choices=(
            ('estandar', _('Estandar')),
            ('reduced', _('Reduced Rate')),
            ('zero', _('Zero Rate'))
        ),
    )

    def __str__(self):
        return f"{self.destination_detail}-general"

    class Meta:
        verbose_name_plural = _('Detalles generales')
        verbose_name = _('Detalle general')


class InventarioDetail(models.Model):
    destination_detail = models.OneToOneField(
        DestinationDetail,
        related_name='inventario',
        on_delete=models.CASCADE,
        verbose_name=_('Detalle del destino'),
    )

    sku = models.CharField(
        _('SKU'),
        max_length=60,
    )

    manager = models.BooleanField(
        _('¿Gestión de inventario?'),
        default=False,
        help_text=_('Activa la gestión de inventario por cada producto'),
    )

    quantity = models.IntegerField(
        _('Cantidad de inventario'),
        blank=True,
        null=True,
        default=0,
    )

    reserva = models.CharField(
        _('¿Permitir reservas?'),
        max_length=50,
        default='no',
        choices=(
            ('no', _('No permitir')),
            ('notify', _('Permitir, pero se avisara al cliente')),
            ('yes', _('Permitir'))
        ),
    )

    umb_exist = models.IntegerField(
        _('Umbral de pocas existencias'),
        blank=True,
        null=True,
        default=0,
    )

    sold_individually = models.BooleanField(
        _('Vendido individualmente'),
        default=False,
        help_text=_(
            'Activa esto para permitir que solo se pueda comprar uno de estos '
            'artículos en cada pedido'),
        )

    def __str__(self):
        return f"{self.destination_detail}-inventario"

    class Meta:
        verbose_name_plural = _('Detalles de inventario')
        verbose_name = _('Detalle de inventario')


class BookingDetail(models.Model):
    destination_detail = models.ForeignKey(
        DestinationDetail,
        related_name='booking',
        on_delete=models.CASCADE,
        verbose_name=_("Detalle del destino"),
    )

    start_date = models.DateField(
        _('Start date'),
        blank=True,
        null=True,
    )

    end_date = models.DateField(
        _('End date'),
        blank=True,
        null=True,
    )

    days = DaysCommaField(
        default=[],
        null=True,
        verbose_name=_('Días'),
    )

    number_ticket = models.IntegerField(
        _('Number of tickets per tour'),
        blank=True,
        null=True,
    )

    special_price = MoneyField(
        _('Special price'),
        max_digits=19,
        decimal_places=4,
        default_currency='USD',
        default=Money(0, 'USD'),
    )

    mode = models.CharField(
        _('Mode'),
        max_length=50,
        default='default',
        choices=(
            ('default', _('Week days')),
            ('exact-dates', _('Exact dates'))
        ),
    )

    is_active = models.CharField(
        _('Is active'),
        max_length=3,
        default='0',
        choices=(
            ('0', _('No')),
            ('1', _('Yes'))
        ),
    )

    def __str__(self):
        return f"{self.destination_detail}-booking-{self.pk}"

    class Meta:
        ordering = ('start_date', 'end_date')
        verbose_name_plural = _('Booking details')
        verbose_name = _('Booking detail')
