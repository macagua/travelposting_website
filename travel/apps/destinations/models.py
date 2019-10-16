from django.db import models
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from easy_thumbnails.fields import ThumbnailerImageField
from apps.accounts.models import CustomerUser
from apps.destinations.fields import DaysCommaField
from apps.destinations.utils import TEMPLATE_DESCRIPTION


class Categorie(models.Model):
    name = models.CharField(
        _('name'),
        max_length=50,
    )

    alias = models.CharField(
        _('Alias'),
        null=True,
        blank=True,
        max_length=20,
    )

    short_description= models.CharField(
        _('Short Description'),
        max_length=50,
    )

    image =  models.ImageField(
        _('Image'),
        upload_to="gallery/categorie/",
    )

    status = models.BooleanField(
        _('Status'),
        default=True
    )

    def __str__(self):
        return f'{self.name}'


class Destination(models.Model):
    categorie = models.ManyToManyField(
        Categorie,
        verbose_name=_("Categorie"),
        blank=True,
    )

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
    )

    departure_date = models.DateField(
        blank=True,
        null=True,
    )
    arrival_date = models.DateField(
        blank=True,
        null=True,
    )

    departure_time = models.TimeField(
        blank = True,
        null = True,
    )

    arrival_time = models.TimeField(
        blank = True,
        null = True,
    )

    number_of_reservations = models.IntegerField(
        blank = True,
        null = True,
    )

    transfer_from = models.TextField(
        max_length = 120,
        blank = True,
        null = True,
    )

    tour_include = models.TextField(
        blank = True,
    )

    tour_not_include = models.TextField(
        blank = True,
    )

    is_published = models.BooleanField(
        _('is_published'),
        default=False,
        editable=False,
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
            pic = '/static/img/travel.png'
        return pic

    @staticmethod
    def count_categorie(alias):
        if alias == 'all':
            return Destination.objects.filter(is_published=True).count()
        else:
            return Destination.objects.filter(is_published=True, categorie__alias=alias).count()

    @property
    def photos(self):
        try:
            list_photos = Photo.objects.filter(destination=self)
        except BaseException:
            return None
        return list_photos

    @property
    def published_date(self):
        try:
            destination_details = GeneralDetail.objects.get(destination_detail__destination=self.pk)
            list_dates = {
                'date_from': destination_details.date_on_sale_from,
                'date_to': destination_details.date_on_sale_to,
            }
        except BaseException:
            return None
        return list_dates

    @property
    def mapa(self):
        mapa = TabData.objects\
        .filter(option_tab__name="Mapa")\
        .get(tour_data__destination=self.pk)
        return mapa

    @property
    def itinerario(self):
        itine = TabData.objects\
        .filter(option_tab__name="Itinerario")\
        .get(tour_data__destination=self.pk)
        return itine


    @property
    def list_prices(self):
        try:
            destination_details = GeneralDetail.objects.get(destination_detail__destination=self.pk)
            list_prices = {
                'regular_price': destination_details.regular_price,
                'sale_price': destination_details.sale_price,
            }
        except BaseException:
            return None
        return list_prices


class DestinationMap(models.Model):
    destination = models.OneToOneField(
        Destination,
        related_name='map',
        on_delete=models.CASCADE,
        verbose_name=_('Map Destination'),
    )
    description_map = models.CharField(
        max_length = 50
    )
    map_destinie = models.PointField(help_text="To generate the map for your location")

    def __unicode__(self):
        return self.map_destinie


    def __str__(self):
        return f'{self.destination} {self.description_map}'


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


class DestinationRating(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        verbose_name=_('Destination Rating'),
    )


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


class Itinerary(models.Model):
    """
    Modelo para itinerario de destinos
    """
    destination = models.ForeignKey(
        Destination,
        on_delete = models.CASCADE,
        verbose_name = _("Itinerary")
    )

    short_description = models.CharField(
        _('Short Description'),
        max_length=50,

    )

    detail_itinerary = models.TextField(
        _('Detail Itinerary'),
    )


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
        decimal_places=2,
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
        decimal_places=2,
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




class SearchLanding(models.Model):
    names = models.CharField(
        'Names',
        null=True,
        blank=True,
        max_length=40
    )

    country = models.CharField(
        'Countries',
        null=True,
        blank=True,
        max_length=30
    )

    email = models.EmailField(
        'Email',
        null=True,
        blank=True,
        max_length=50
    )

    whatsapp = models.CharField(
        'Whatsapp',
        null=True,
        blank=True,
        max_length=30
    )

    def __str__(self):
        return f"{self.email}-{self.country}"

    class Meta:
        ordering = ('email', 'country')
        verbose_name_plural = _('Search Landing')
        verbose_name = _('Search Landing')


class Booking(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=False,
    )

    firts_name = models.CharField(
        _('Firts Name'),
        null=False,
        blank=False,
        max_length = 50
    )

    last_name = models.CharField(
        _('Last Name'),
        null=False,
        blank=False,
        max_length = 50
    )

    dni = models.CharField(
        _('Identity number'),
        null=True,
        blank=True,
        max_length = 50
    )

    cellphone = models.CharField(
        _('Cellphone'),
        null=False,
        blank=False,
        max_length = 50
    )

    mail = models.EmailField(
        _('Email'),
        null=True,
        blank=True,
        max_length = 100,
    )

    number_travel = models.CharField(
        _('Number of people travelling'),
        null=True,
        blank=True,
        max_length= 2,
    )

    name_booking = models.CharField(
        _('Booking'),
        null=True,
        blank= True,
        max_length = 50,
    )

    comment = models.TextField(
        _('Comment'),
        blank=True,
        null=True,
    )

    seen_status = models.BooleanField(
        _('seen'),
        default=False,
    )

    process_status = models.BooleanField(
        _('status'),
        default=False,
        help_text=_('Means if receive following or not.'),
    )

    def __str__(self):
        return f"{self.firts_name}-{self.last_name}"

    class Meta:
        verbose_name_plural = _("Booking's")
        verbose_name = _('Booking')

class BookingStats(models.Model):
    booking = models.ForeignKey(Booking,
                on_delete=False,
                verbose_name=_("Booking")
    )
    user = models.ForeignKey(
        CustomerUser,
        on_delete=False,
        verbose_name=_("Users"),
    )
    date = models.DateTimeField(_("Datetime"),auto_now=True)

    def __str__(self):
        return f"{self.booking}-{self.user}-{self.date}"

    class Meta:
        verbose_name_plural = _("Booking Stats")
        verbose_name = _("Booking Stast")
    
