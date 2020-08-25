from django.db import models
from django.contrib.gis.db import models
from django.db.models import Count, Max, F
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from easy_thumbnails.fields import ThumbnailerImageField
from apps.accounts.models import CustomerUser, COUNTRIES
from apps.destinations.fields import DaysCommaField
from apps.destinations.utils import TEMPLATE_DESCRIPTION
from filer.fields.image import FilerImageField
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime



TEMPLATE_DESCRIPTION = _("""
<strong>Who we are</strong><br><br>

<p><b>Please enter your text here...</b></p><br><br>

<strong>Mission</strong><br><br>

<p><b>Please enter your text here...</b></p><br><br>

<table class='table table-bordered tours-tabs__table'
       style='width: 100%px;'>
<tbody>
<tr>
<td style='width: 213px;'><strong>EXIT / RETURN</strong></td>
<td style='width: 574.233px;'><b>Enter the exit here...</b></td>
</tr>
<tr>
<td style='width: 213px;'><strong>EXIT TIME</strong></td>
<td style='width: 574.233px;'><b>Enter the time of exit here...</b></td>
</tr>
<tr>
<td style='width: 213px;'><strong>ARRIVAL TIME</strong></td>
<td style='width: 574.233px;'><b>Enter the time of arrival here...</b></td>
</tr>
<tr>
<td style='width: 213px;'><strong>NR. OF TOUR FOR RESERVATIONS</strong></td>
<td style='width: 574.233px;'><b>Enter the tour number here...</b></td>
</tr>
<tr>
<td style='width: 213px;'><strong>TRANSFER FROM </strong></td>
<td style='width: 574.233px;'><strong><b>Enter the transfer here...</b></strong></td>
</tr>
</tbody>
</table>
""")


class Categorie(models.Model):
    name = models.CharField(
        _('Name'),
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

    class Meta:
        verbose_name_plural = _('Categories')
        verbose_name = _('Category')

    def __str__(self):
        return f'{self.name}'


class Destination(models.Model):
    categorie = models.ManyToManyField(
        Categorie,
        verbose_name=_("Categories"),
        blank=True,
    )

    user = models.ForeignKey(
        CustomerUser,
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )

    name = models.CharField(
        _('Name'),
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
        _('Description'),
        blank=True,
        null=True,
        default=TEMPLATE_DESCRIPTION,
    )

    departure_date = models.DateField(
        _('Departure Date'),
        blank=True,
        null=True,
    )
    arrival_date = models.DateField(
        _('Arrival Date'),
        blank=True,
        null=True,
    )

    departure_time = models.TimeField(
        _('Departure Time'),
        blank = True,
        null = True,
    )

    arrival_time = models.TimeField(
        _('Arrival Time'),
        blank = True,
        null = True,
    )

    number_of_reservations = models.IntegerField(
        _('Number of Reservations'),
        blank = True,
        null = True,
    )

    transfer_from = models.TextField(
        _('Transfer from'),
        max_length = 120,
        blank = True,
        null = True,
    )

    tour_include = models.TextField(
        _('Tour include'),
        blank = True,
    )

    tour_not_include = models.TextField(
        _('Tour not include'),
        blank = True,
    )

    is_published = models.BooleanField(
        _('is published?'),
        default=False,
        editable=False,
    )

    is_deleted = models.BooleanField(
        _('is deleted?'),
        default=False,
        editable=False,
    )

    has_wifi = models.BooleanField(
        _("Destination has Wifi?"),
        default=False,
    )

    has_breakfast_incluided = models.BooleanField(
        _("Destination has Breakfast included?"),
        default=False,
    )

    has_gym = models.BooleanField(
        _("Destination has Gym?"),
        default=False,
    )

    has_air_conditioning = models.BooleanField(
        _("Destination has Air conditioning?"),
        default=False,
    )

    has_restaurant = models.BooleanField(
        _("Destination has Restaurant?"),
        default=False,
    )

    has_bar = models.BooleanField(
        _("Destination has Bar?"),
        default=False,
    )

    has_housekeeping = models.BooleanField(
        _("Destination has Housekeeping service?"),
        default=False,
    )

    has_room_service = models.BooleanField(
        _("Destination has Room service?"),
        default=False,
    )

    has_business_services = models.BooleanField(
        _("Destination has Business services?"),
        default=False,
    )

    has_hob_tub = models.BooleanField(
        _("Destination has Hob Tub?"),
        default=False,
    )

    has_front_desk = models.BooleanField(
        _("Destination has 25/7 Front Desk?"),
        default=False,
    )

    has_laundry = models.BooleanField(
        _("Destination has Laundry service?"),
        default=False,
    )

    social_network = models.BooleanField(
        _('Social Network'),
        default=False,
        help_text = _("If you check this option it will show the social networks of the destination"),
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Destination")
        verbose_name_plural = _("Destinations")
        ordering = ('user',)
        unique_together = ('user', 'name',)

    def __str__(self):
        return f'{self.name}'

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
    def videos(self):
        try:
            list_videos = Video.objects.filter(destination=self)
        except BaseException:
            return None
        return list_videos

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
        .filter(option_tab__name="Map")\
        .get(tour_data__destination=self.pk)
        return mapa

    @property
    def itinerario(self):
        itine = TabData.objects\
        .filter(option_tab__name="Itinerary")\
        .get(tour_data__destination=self.pk)
        return itine

    @property
    def itinerario2(self):
        it2 =   Itinerary.objects.get(destination=self.pk)
        return it2

    @property
    def social(self):
        sn = SocialNetwork.objects.get(destination=self.pk)
        return sn

    @property
    def customer(self):
        user = CustomerUser.objects.get(destination=self.pk)
        return user

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
    description_map = models.CharField(_('Description Map'),
        max_length = 50
    )
    map_destinie = models.PointField(_('Destination Map'),
        help_text=_("To generate the map for your location"))

    class Meta:
        verbose_name = _('Destination Map')
        verbose_name_plural = _('Destination Maps')

    def __unicode__(self):
        return self.map_destinie

    def __str__(self):
        return f'{self.destination} {self.description_map}'


class Photo(models.Model):
    destination = models.ForeignKey(
        Destination,
        related_name='gallery',
        on_delete=models.CASCADE,
        verbose_name=_('Destination'),
    )

    name = models.CharField(
        _('Name'),
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
        _('Description'),
        blank=True,
        null=True,
        default=_("No comment"),
    )

    thumbnail = ThumbnailerImageField(
        _('Thumbnail'),
        upload_to="gallery/thumbnail/",
        blank=True,
        null=True,
    )

    image = models.ImageField(
        _('Image'),
        upload_to="gallery/image/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('sort', 'name')
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')

    def __str__(self):
        return f"{self.name}"


class Video(models.Model):
    destination = models.ForeignKey(
        Destination,
        related_name='media',
        on_delete=models.CASCADE,
        verbose_name=_('Destination'),
    )

    name = models.CharField(
        _('Name'),
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
        _('Description'),
        blank=True,
        null=True,
        default=_("No comment"),
    )

    thumbnail_preview = ThumbnailerImageField(
        _('Thumbnail'),
        blank=True,
        null=True,
        upload_to="gallery/thumbnail/",
    )

    video = models.FileField(
        _("Video"),
        blank=True,
        null=True,
        upload_to="gallery/video/",
        # validators=[valid_extension]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('sort', 'name')
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')


class DestinationRating(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        verbose_name=_('Destination Rating'),
    )

    class Meta:
        verbose_name = _('Destination Rating')
        verbose_name_plural = _('Destinations Rating')

    def __str__(self):
        return f"{self.destination}"


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
        verbose_name=_('Destination'),
    )

    badge = models.CharField(
        _('Badge'),
        max_length=150,
        blank=True,
        null=True,
        choices=(
            ('1', _('Last minute')),
            ('2', _('Deal of the Month')),
            ('3', _('FamTrip')),
            ('4', _('Congresses')),
            ('5', _('Events')),
            ('6', _('Hotel')),
            ('7', _('Mobility')),
            ('8', _('Leisure +')),
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

    def __str__(self):
        return f'{self.destination}-{self.short_description}'

    class Meta:
        verbose_name = _('Itinerary')
        verbose_name_plural = _('Itineraries')


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
        _('Name'),
        max_length=150,
    )

    description = models.TextField(
        _('Description'),
        blank=True,
        null=True,
    )

    template = models.TextField(
        _('Template'),
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name',)
        verbose_name_plural = _('Tab options')
        verbose_name = _('Tab option')


class HeaderSection(models.Model):
    destination = models.OneToOneField(
        Destination,
        related_name='header',
        on_delete=models.CASCADE,
        verbose_name=_('Destination'),
    )

    display_mode = models.CharField(
        _('Display mode'),
        max_length=15,
        default='hide',
        choices=(
            ('hide', _('Default')),
            ('banner', _('Image')),
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
        _('Image'),
        upload_to='header/images',
        blank=True,
        null=True,
    )

    parallax = models.BooleanField(
        _('Parallax'),
        default=True,
    )

    image_repeat = models.CharField(
        _('Image repeat'),
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

    class Meta:
        verbose_name_plural = _('Header sections')
        verbose_name = _('Header section')

    def __str__(self):
        return f"{self.subtitle}"


class DestinationDetail(models.Model):
    destination = models.OneToOneField(
        Destination,
        related_name='details',
        on_delete=models.CASCADE,
        verbose_name=_('Destination'),
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
        _('Downloadable'),
        default=False,
    )

    class Meta:
        verbose_name_plural = _('Destination details')
        verbose_name = _('Destination detail')

    def __str__(self):
        return f"{self.destination}-details"


class GeneralDetail(models.Model):
    destination_detail = models.OneToOneField(
        DestinationDetail,
        related_name='general',
        on_delete=models.CASCADE,
        verbose_name=_('Destination detail'),
    )

    regular_price = MoneyField(
        _('Normal price'),
        max_digits=19,
        decimal_places=2,
        default_currency='USD',
        default=Money(0, 'USD'),
    )

    sale_price = MoneyField(
        _('Reduced price'),
        max_digits=19,
        decimal_places=2,
        default_currency='USD',
        default=Money(0, 'USD'),
    )

    date_on_sale_from = models.DateField(
        _('Initial discount date'),
        blank=True,
        null=True,
    )

    date_on_sale_to = models.DateField(
        _('Final discount date'),
        blank=True,
        null=True,
    )

    status_imp = models.CharField(
        _('Tax status'),
        max_length=50,
        default='imponible',
        choices=(
            ('imponible', _('Impossible')),
            ('envio', _('Shipping only')),
            ('ninguno', _('None'))
        ),
    )

    class_imp = models.CharField(
        _('Tax type'),
        max_length=50,
        default='estandar',
        choices=(
            ('estandar', _('Standard')),
            ('reduced', _('Reduced Rate')),
            ('zero', _('Zero Rate'))
        ),
    )

    class Meta:
        verbose_name_plural = _('General details')
        verbose_name = _('General detail')

    def __str__(self):
        return f"{self.destination_detail}-general"


class InventarioDetail(models.Model):
    destination_detail = models.OneToOneField(
        DestinationDetail,
        related_name='inventario',
        on_delete=models.CASCADE,
        verbose_name=_('Destination detail'),
    )

    sku = models.CharField(
        _('SKU'),
        max_length=60,
    )

    manager = models.BooleanField(
        _('Inventory management?'),
        default=False,
        help_text=_('Activate inventory management for each product'),
    )

    quantity = models.IntegerField(
        _('Inventory quantity'),
        blank=True,
        null=True,
        default=0,
    )

    reserva = models.CharField(
        _('Allow reservations?'),
        max_length=50,
        default='no',
        choices=(
            ('no', _('Do not allow')),
            ('notify', _('Allow, but the customer will be warned')),
            ('yes', _('Allow'))
        ),
    )

    umb_exist = models.IntegerField(
        _('Low stock threshold'),
        blank=True,
        null=True,
        default=0,
    )

    sold_individually = models.BooleanField(
        _('Sold individually'),
        default=False,
        help_text=_(
            'Activate this to allow only one of these '
            'items to be purchased in each order'),
        )

    class Meta:
        verbose_name_plural = _('Inventory details')
        verbose_name = _('Inventory detail')

    def __str__(self):
        return f"{self.destination_detail}-inventario"


class BookingDetail(models.Model):
    destination_detail = models.ForeignKey(
        DestinationDetail,
        related_name='booking',
        on_delete=models.CASCADE,
        verbose_name=_("Destination detail"),
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
        verbose_name=_('Days'),
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
        blank=True,
        null=True,
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

    class Meta:
        ordering = ('start_date', 'end_date')
        verbose_name_plural = _('Booking details')
        verbose_name = _('Booking detail')

    def __str__(self):
        return f"{self.destination_detail}-booking-{self.pk}"


class SearchLanding(models.Model):
    names = models.CharField(
        _('Names'),
        null=True,
        blank=True,
        max_length=40
    )

    country = models.CharField(
        _('Countries'),
        null=True,
        blank=True,
        max_length=30
    )

    email = models.EmailField(
        _('Email'),
        null=True,
        blank=True,
        max_length=50
    )

    whatsapp = models.CharField(
        _('Whatsapp'),
        null=True,
        blank=True,
        max_length=30
    )

    class Meta:
        ordering = ('email', 'country')
        verbose_name_plural = _('Search Landing')
        verbose_name = _('Search Landing')

    def __str__(self):
        return f"{self.email}-{self.country}"


class Booking(models.Model):
    destination = models.ForeignKey(
        Destination,
        verbose_name = _("Destination"),
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

    class Meta:
        verbose_name_plural = _("Booking's")
        verbose_name = _('Booking')

    def __str__(self):
        return f"{self.firts_name}-{self.last_name}"


class BookingStats(models.Model):
    booking = models.ForeignKey(
        Booking,
        verbose_name=_("Booking"),
        on_delete=False,
    )

    user = models.ForeignKey(
        CustomerUser,
        on_delete=False,
        verbose_name=_("Users"),
    )

    date = models.DateTimeField(_("Datetime"),auto_now=True)

    class Meta:
        verbose_name_plural = _("Booking Stats")
        verbose_name = _("Booking Stast")

    def __str__(self):
        return f"{self.booking}-{self.user}-{self.date}"



class SocialNetwork(models.Model):
    destination = models.ForeignKey(Destination,
        verbose_name = _("Destination"), on_delete=models.CASCADE)
    social_network = models.BooleanField(
        _('Social Network'),
        default=False,
        help_text = _("Check for use the network from user"),
    )
    facebook = models.CharField(_("Facebook"), max_length=100, null=True, blank=True)
    instagram = models.CharField(_("Instagram"), max_length=100, null=True, blank=True)
    twitter = models.CharField(_("Twitter"), max_length=100, null=True, blank=True)
    linkedin = models.CharField(_("Linkedin"), max_length=100, null=True, blank=True)
    pinterest = models.URLField(_("Pinterest"), max_length=100, null=True, blank=True)
    website = models.URLField(_("Website"), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = _("Social Networks")
        verbose_name = _("Social Network")

    def __str__(self):
        return f"{self.destination}"


class DestinationVisitor(models.Model):
    destination = models.ForeignKey(Destination,
        verbose_name = _("Destination"), related_name='visitor',
        on_delete = models.CASCADE)
    ip_address = models.CharField(_("IP Address"), max_length = 100)
    dma_code = models.IntegerField(_("Dma Code"), blank = True, null = True)
    country_code = models.CharField(_("Country Code"), max_length = 5)
    country_name = models.CharField(_("Country Name"), max_length = 100)
    date_time = models.DateTimeField(_("Date/time"), auto_now_add = True)

    class Meta:
        verbose_name = _('Destination Visitor')
        verbose_name_plural = _('Destination Visitors')

    def __str__(self):
        return f"{self.destination}-{self.country_code}-{self.country_code}"


class Advertising(models.Model):

    POSITION = (
        (1, _('Up')),
        (2, _('Middle')),
        (2, _('Down')),
    )

    name = models.CharField(_('Name'), max_length=30, blank=True)
    company = models.CharField(_('Company'), max_length=30, blank=True)
    imagen_desktop = FilerImageField(related_name='desktop',
                                    null=True,
                                    blank=True,
                                    on_delete=False,
                                    verbose_name=_("Desktop Image"),
                                    help_text=_('Image to be displayed in desktop resolutions'))
    imagen_mobile = FilerImageField(related_name='mobile',
                                    null=True,
                                    blank=True,
                                    on_delete=False,
                                    verbose_name=_("Mobile Image"),
                                    help_text=_('Image to be displayed in mobile resolution'))
    position = models.IntegerField(_('Position'), choices=POSITION, default=1)
    from_date = models.DateField(_('Start of advertising'),
                             default=datetime.date.today)
    to_date = models.DateField(_('End of advertising'), default=datetime.date.today)
    status = models.BooleanField(_('Active'), default=False, help_text=(
        _('Indicate Advertising Status')))
    url = models.URLField(_('URL'), max_length=200, blank=False)
    created_on = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        db_table='Advertising'
        verbose_name_plural = _('Ads')
        verbose_name = _('Advertising')

    def __str__(self):
        return self.name


# A private directmessage on the dashboard
class MessageDashboard(models.Model):
    subject = models.CharField(
        _('Subject'), blank=False, null=False, max_length=1000)
    content = models.TextField(_('Content'))
    sender = models.ForeignKey(
        CustomerUser, related_name='dash_sender', verbose_name=_("Sender"), on_delete=models.CASCADE)
    # the variable recipient will be active when we'll work that the group
    recipient = models.ForeignKey(CustomerUser, related_name='dash_recipient', verbose_name=_("Recipient"), on_delete=models.CASCADE)
    sent_at = models.DateTimeField(_("sent at"), null=True, blank=True)
    read_at = models.DateTimeField(_("read at"), null=True, blank=True)

    class Meta:
        verbose_name_plural = _('Messages Dashboard')
        verbose_name = _('Message Dashboard')

    @property
    def unread(self):
        """returns whether the message was read or not"""
        if self.read_at is not None:
            return False
        return True

    def __str__(self):
        return self.content

    def save(self, **kwargs):
        if self.sender == self.recipient:
            raise ValidationError(_("You can't send messages to yourself"))

        if not self.id:
            self.sent_at = timezone.now()
        super(MessageDashboard, self).save(**kwargs)


# Petitions
class Request(models.Model):
    MANAGER = 'MGR'
    AGENCY = 'AGC'
    TYPES = (
            (MANAGER, 'Manager'),
            (AGENCY, 'Agency'),
            )
    PENDING = 'PEND'
    APPROVED = 'APPR'
    REJECTED = 'REJE'
    STATUS = (
            (PENDING, 'Pending'),
            (APPROVED, 'Approved'),
            (REJECTED, 'Rejected'),
            )
    user = models.ForeignKey(
            CustomerUser,
            on_delete=models.CASCADE,
            verbose_name=_("User"),
    )

    country = models.CharField(
        'Countries',
        choices=COUNTRIES,
        max_length=3
    )

    type = models.CharField(
            max_length=3, 
            default=AGENCY,
            choices=TYPES)

    status = models.CharField(
            default=PENDING,
            max_length=4,
            choices=STATUS)

    class Meta:
        unique_together = ('user', 'country')


    def __str__(self):
        return '%s %s' % (self.country, self.get_type_display())


class BookingQuestion(models.Model):
    question_text = models.CharField(_("Question text"), max_length=200)
    pub_date = models.DateTimeField(_("date published"))

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
            return self.question_text

    class Meta:
        verbose_name = _("Booking Question")
        verbose_name_plural = _("Booking Questions")


class BookingChoice(models.Model):
    question = models.ForeignKey(BookingQuestion, verbose_name=_("Question"), on_delete=models.CASCADE)
    choice_text = models.CharField(_("Choice text"), max_length=200)
    votes = models.IntegerField(_("Votes"), default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = _("Booking Choice")
        verbose_name_plural = _("Booking Choices")
