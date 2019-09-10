# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WpAalbAsinResponse(models.Model):
    asin = models.CharField(primary_key=True, max_length=10)
    marketplace = models.CharField(max_length=5)
    item_lookup_response = models.TextField(blank=True, null=True)
    last_updated_time = models.DateTimeField(blank=True, null=True)
    last_access_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_Aalb_Asin_Response'
        unique_together = (('asin', 'marketplace'),)


class WpAdventureToursStorage(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_id = models.BigIntegerField()
    storage_key = models.CharField(max_length=50)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_adventure_tours_storage'


class WpAndroappStats(models.Model):
    title = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    eligible = models.IntegerField(blank=True, null=True)
    ios_eligible = models.IntegerField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    notregistered = models.IntegerField(db_column='notRegistered', blank=True, null=True)  # Field name made lowercase.
    mismatchsenderid = models.IntegerField(blank=True, null=True)
    other = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=60, blank=True, null=True)
    ios_bulk_sent = models.IntegerField(blank=True, null=True)
    ios_sent = models.IntegerField(blank=True, null=True)
    ios_notregistered = models.IntegerField(db_column='ios_notRegistered', blank=True, null=True)  # Field name made lowercase.
    bulk_sent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_androapp_stats'


class WpCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_commentmeta'


class WpComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_comments'


class WpContactformmaker(models.Model):
    title = models.CharField(max_length=127)
    mail = models.CharField(max_length=256)
    form_front = models.TextField()
    theme = models.IntegerField()
    submit_text = models.TextField()
    url = models.CharField(max_length=256)
    submit_text_type = models.IntegerField()
    script_mail = models.TextField()
    script_mail_user = models.TextField()
    counter = models.IntegerField()
    published = models.IntegerField()
    label_order = models.TextField()
    label_order_current = models.TextField()
    article_id = models.CharField(max_length=500)
    public_key = models.CharField(max_length=50)
    private_key = models.CharField(max_length=50)
    recaptcha_theme = models.CharField(max_length=20)
    form_fields = models.TextField()
    savedb = models.IntegerField()
    sendemail = models.IntegerField()
    requiredmark = models.CharField(max_length=20)
    mail_from = models.CharField(max_length=128)
    mail_from_name = models.CharField(max_length=128)
    reply_to = models.CharField(max_length=128)
    send_to = models.CharField(max_length=128)
    autogen_layout = models.IntegerField()
    custom_front = models.TextField()
    mail_from_user = models.CharField(max_length=128)
    mail_from_name_user = models.CharField(max_length=128)
    reply_to_user = models.CharField(max_length=128)
    disabled_fields = models.CharField(max_length=200)
    mail_cc = models.CharField(max_length=128)
    mail_cc_user = models.CharField(max_length=128)
    mail_bcc = models.CharField(max_length=128)
    mail_bcc_user = models.CharField(max_length=128)
    mail_subject = models.CharField(max_length=128)
    mail_subject_user = models.CharField(max_length=128)
    mail_mode = models.IntegerField()
    mail_mode_user = models.IntegerField()
    wpmail = models.IntegerField()
    sortable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_contactformmaker'


class WpContactformmakerBlocked(models.Model):
    ip = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'wp_contactformmaker_blocked'


class WpContactformmakerSubmits(models.Model):
    form_id = models.IntegerField()
    element_label = models.CharField(max_length=128)
    element_value = models.CharField(max_length=600)
    group_id = models.IntegerField()
    date = models.DateTimeField()
    ip = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'wp_contactformmaker_submits'


class WpContactformmakerThemes(models.Model):
    title = models.CharField(max_length=200)
    css = models.TextField()
    default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_contactformmaker_themes'


class WpContactformmakerViews(models.Model):
    form_id = models.IntegerField(primary_key=True)
    views = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_contactformmaker_views'


class WpEmBookings(models.Model):
    booking_id = models.BigAutoField(primary_key=True)
    event_id = models.BigIntegerField(blank=True, null=True)
    person_id = models.BigIntegerField()
    booking_spaces = models.IntegerField()
    booking_comment = models.TextField(blank=True, null=True)
    booking_date = models.DateTimeField()
    booking_status = models.IntegerField()
    booking_price = models.DecimalField(max_digits=14, decimal_places=4)
    booking_tax_rate = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    booking_taxes = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    booking_meta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_em_bookings'


class WpEmEvents(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    event_slug = models.CharField(max_length=200, blank=True, null=True)
    event_owner = models.BigIntegerField(blank=True, null=True)
    event_status = models.IntegerField(blank=True, null=True)
    event_name = models.TextField(blank=True, null=True)
    event_start_time = models.TimeField(blank=True, null=True)
    event_end_time = models.TimeField(blank=True, null=True)
    event_all_day = models.IntegerField(blank=True, null=True)
    event_start_date = models.DateField(blank=True, null=True)
    event_end_date = models.DateField(blank=True, null=True)
    post_content = models.TextField(blank=True, null=True)
    event_rsvp = models.IntegerField()
    event_rsvp_date = models.DateField(blank=True, null=True)
    event_rsvp_time = models.TimeField(blank=True, null=True)
    event_rsvp_spaces = models.IntegerField(blank=True, null=True)
    event_spaces = models.IntegerField(blank=True, null=True)
    event_private = models.IntegerField()
    location_id = models.BigIntegerField(blank=True, null=True)
    recurrence_id = models.BigIntegerField(blank=True, null=True)
    event_category_id = models.BigIntegerField(blank=True, null=True)
    event_attributes = models.TextField(blank=True, null=True)
    event_date_created = models.DateTimeField(blank=True, null=True)
    event_date_modified = models.DateTimeField(blank=True, null=True)
    recurrence = models.IntegerField(blank=True, null=True)
    recurrence_interval = models.IntegerField(blank=True, null=True)
    recurrence_freq = models.TextField(blank=True, null=True)
    recurrence_byday = models.TextField(blank=True, null=True)
    recurrence_byweekno = models.IntegerField(blank=True, null=True)
    recurrence_days = models.IntegerField(blank=True, null=True)
    recurrence_rsvp_days = models.IntegerField(blank=True, null=True)
    blog_id = models.BigIntegerField(blank=True, null=True)
    group_id = models.BigIntegerField(blank=True, null=True)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    event_timezone = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_em_events'


class WpEmLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    blog_id = models.BigIntegerField(blank=True, null=True)
    location_slug = models.CharField(max_length=200, blank=True, null=True)
    location_name = models.TextField(blank=True, null=True)
    location_owner = models.BigIntegerField()
    location_address = models.CharField(max_length=200, blank=True, null=True)
    location_town = models.CharField(max_length=200, blank=True, null=True)
    location_state = models.CharField(max_length=200, blank=True, null=True)
    location_postcode = models.CharField(max_length=10, blank=True, null=True)
    location_region = models.CharField(max_length=200, blank=True, null=True)
    location_country = models.CharField(max_length=2, blank=True, null=True)
    location_latitude = models.FloatField(blank=True, null=True)
    location_longitude = models.FloatField(blank=True, null=True)
    post_content = models.TextField(blank=True, null=True)
    location_status = models.IntegerField(blank=True, null=True)
    location_private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_em_locations'


class WpEmMeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    object_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)
    meta_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_em_meta'


class WpEmTickets(models.Model):
    ticket_id = models.BigAutoField(primary_key=True)
    event_id = models.BigIntegerField()
    ticket_name = models.TextField()
    ticket_description = models.TextField(blank=True, null=True)
    ticket_price = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    ticket_start = models.DateTimeField(blank=True, null=True)
    ticket_end = models.DateTimeField(blank=True, null=True)
    ticket_min = models.IntegerField(blank=True, null=True)
    ticket_max = models.IntegerField(blank=True, null=True)
    ticket_spaces = models.IntegerField(blank=True, null=True)
    ticket_members = models.IntegerField(blank=True, null=True)
    ticket_members_roles = models.TextField(blank=True, null=True)
    ticket_guests = models.IntegerField(blank=True, null=True)
    ticket_required = models.IntegerField(blank=True, null=True)
    ticket_meta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_em_tickets'


class WpEmTicketsBookings(models.Model):
    ticket_booking_id = models.BigAutoField(primary_key=True)
    booking_id = models.BigIntegerField()
    ticket_id = models.BigIntegerField()
    ticket_booking_spaces = models.IntegerField()
    ticket_booking_price = models.DecimalField(max_digits=14, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'wp_em_tickets_bookings'


class WpFailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    job = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_failed_jobs'


class WpFb3DPages(models.Model):
    page_id = models.BigAutoField(db_column='page_ID', primary_key=True)  # Field name made lowercase.
    page_post_id = models.BigIntegerField(db_column='page_post_ID')  # Field name made lowercase.
    page_title = models.TextField()
    page_source_type = models.CharField(max_length=20)
    page_source_data = models.TextField()
    page_thumbnail_type = models.CharField(max_length=20)
    page_thumbnail_data = models.TextField()
    page_meta_data = models.TextField()
    page_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_fb3d_pages'


class WpFormmaker(models.Model):
    title = models.CharField(max_length=127)
    mail = models.CharField(max_length=128)
    form_front = models.TextField()
    theme = models.IntegerField()
    javascript = models.TextField()
    submit_text = models.TextField()
    url = models.CharField(max_length=200)
    submit_text_type = models.IntegerField()
    script_mail = models.TextField()
    script_mail_user = models.TextField()
    counter = models.IntegerField()
    published = models.IntegerField()
    label_order = models.TextField()
    label_order_current = models.TextField()
    article_id = models.CharField(max_length=500)
    pagination = models.CharField(max_length=128)
    show_title = models.CharField(max_length=128)
    show_numbers = models.CharField(max_length=128)
    public_key = models.CharField(max_length=50)
    private_key = models.CharField(max_length=50)
    recaptcha_theme = models.CharField(max_length=20)
    paypal_mode = models.IntegerField()
    checkout_mode = models.CharField(max_length=20)
    paypal_email = models.CharField(max_length=50)
    payment_currency = models.CharField(max_length=20)
    tax = models.FloatField()
    form_fields = models.TextField()
    savedb = models.IntegerField()
    sendemail = models.IntegerField()
    requiredmark = models.CharField(max_length=20)
    from_mail = models.CharField(max_length=128)
    from_name = models.CharField(max_length=128)
    reply_to = models.CharField(max_length=128)
    send_to = models.CharField(max_length=128)
    autogen_layout = models.IntegerField()
    custom_front = models.TextField()
    mail_from_user = models.CharField(max_length=128)
    mail_from_name_user = models.CharField(max_length=128)
    reply_to_user = models.CharField(max_length=128)
    condition = models.TextField()
    mail_cc = models.CharField(max_length=128)
    mail_cc_user = models.CharField(max_length=128)
    mail_bcc = models.CharField(max_length=128)
    mail_bcc_user = models.CharField(max_length=128)
    mail_subject = models.CharField(max_length=128)
    mail_subject_user = models.CharField(max_length=128)
    mail_mode = models.IntegerField()
    mail_mode_user = models.IntegerField()
    mail_attachment = models.IntegerField()
    mail_attachment_user = models.IntegerField()
    user_id_wd = models.CharField(max_length=220)
    sortable = models.IntegerField()
    frontend_submit_fields = models.TextField()
    frontend_submit_stat_fields = models.TextField()
    mail_emptyfields = models.IntegerField()
    mail_verify = models.IntegerField()
    mail_verify_expiretime = models.FloatField()
    mail_verification_post_id = models.IntegerField()
    save_uploads = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker'


class WpFormmakerBackup(models.Model):
    backup_id = models.AutoField(primary_key=True)
    cur = models.IntegerField()
    id = models.IntegerField()
    title = models.CharField(max_length=127)
    mail = models.CharField(max_length=128)
    form_front = models.TextField()
    theme = models.IntegerField()
    javascript = models.TextField()
    submit_text = models.TextField()
    url = models.CharField(max_length=200)
    submit_text_type = models.IntegerField()
    script_mail = models.TextField()
    script_mail_user = models.TextField()
    counter = models.IntegerField()
    published = models.IntegerField()
    label_order = models.TextField()
    label_order_current = models.TextField()
    article_id = models.CharField(max_length=500)
    pagination = models.CharField(max_length=128)
    show_title = models.CharField(max_length=128)
    show_numbers = models.CharField(max_length=128)
    public_key = models.CharField(max_length=50)
    private_key = models.CharField(max_length=50)
    recaptcha_theme = models.CharField(max_length=20)
    paypal_mode = models.IntegerField()
    checkout_mode = models.CharField(max_length=20)
    paypal_email = models.CharField(max_length=50)
    payment_currency = models.CharField(max_length=20)
    tax = models.FloatField()
    form_fields = models.TextField()
    savedb = models.IntegerField()
    sendemail = models.IntegerField()
    requiredmark = models.CharField(max_length=20)
    from_mail = models.CharField(max_length=128)
    from_name = models.CharField(max_length=128)
    reply_to = models.CharField(max_length=128)
    send_to = models.CharField(max_length=128)
    autogen_layout = models.IntegerField()
    custom_front = models.TextField()
    mail_from_user = models.CharField(max_length=128)
    mail_from_name_user = models.CharField(max_length=128)
    reply_to_user = models.CharField(max_length=128)
    condition = models.TextField()
    mail_cc = models.CharField(max_length=128)
    mail_cc_user = models.CharField(max_length=128)
    mail_bcc = models.CharField(max_length=128)
    mail_bcc_user = models.CharField(max_length=128)
    mail_subject = models.CharField(max_length=128)
    mail_subject_user = models.CharField(max_length=128)
    mail_mode = models.IntegerField()
    mail_mode_user = models.IntegerField()
    mail_attachment = models.IntegerField()
    mail_attachment_user = models.IntegerField()
    user_id_wd = models.CharField(max_length=220)
    sortable = models.IntegerField()
    frontend_submit_fields = models.TextField()
    frontend_submit_stat_fields = models.TextField()
    mail_emptyfields = models.IntegerField()
    mail_verify = models.IntegerField()
    mail_verify_expiretime = models.FloatField()
    mail_verification_post_id = models.IntegerField()
    save_uploads = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker_backup'


class WpFormmakerBlocked(models.Model):
    ip = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'wp_formmaker_blocked'


class WpFormmakerQuery(models.Model):
    form_id = models.IntegerField()
    query = models.TextField()
    details = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker_query'


class WpFormmakerSessions(models.Model):
    form_id = models.IntegerField()
    group_id = models.IntegerField()
    ip = models.CharField(max_length=20)
    ord_date = models.DateTimeField()
    ord_last_modified = models.DateTimeField()
    status = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    mobile_phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    address = models.CharField(max_length=300)
    paypal_info = models.TextField()
    without_paypal_info = models.TextField()
    ipn = models.CharField(max_length=20)
    checkout_method = models.CharField(max_length=20)
    tax = models.FloatField()
    shipping = models.FloatField()
    shipping_type = models.CharField(max_length=200)
    read = models.IntegerField()
    total = models.FloatField()
    currency = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'wp_formmaker_sessions'


class WpFormmakerSubmits(models.Model):
    form_id = models.IntegerField()
    element_label = models.CharField(max_length=128)
    element_value = models.TextField()
    group_id = models.IntegerField()
    date = models.DateTimeField()
    ip = models.CharField(max_length=128)
    user_id_wd = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker_submits'


class WpFormmakerThemes(models.Model):
    title = models.CharField(max_length=200)
    css = models.TextField()
    default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker_themes'


class WpFormmakerViews(models.Model):
    form_id = models.IntegerField(primary_key=True)
    views = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker_views'


class WpIclCmsNavCache(models.Model):
    id = models.BigAutoField(primary_key=True)
    cache_key = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_icl_cms_nav_cache'


class WpIclContentStatus(models.Model):
    rid = models.BigIntegerField(primary_key=True)
    nid = models.BigIntegerField()
    timestamp = models.DateTimeField()
    md5 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'wp_icl_content_status'


class WpIclCoreStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField()
    module = models.CharField(max_length=16)
    origin = models.CharField(max_length=64)
    target = models.CharField(max_length=64)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_core_status'


class WpIclFlags(models.Model):
    lang_code = models.CharField(unique=True, max_length=10)
    flag = models.CharField(max_length=32)
    from_template = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_flags'


class WpIclLanguages(models.Model):
    code = models.CharField(unique=True, max_length=7)
    english_name = models.CharField(unique=True, max_length=128)
    major = models.IntegerField()
    active = models.IntegerField()
    default_locale = models.CharField(max_length=35, blank=True, null=True)
    tag = models.CharField(max_length=35, blank=True, null=True)
    encode_url = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_languages'


class WpIclLanguagesTranslations(models.Model):
    language_code = models.CharField(max_length=7)
    display_language_code = models.CharField(max_length=7)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_icl_languages_translations'
        unique_together = (('language_code', 'display_language_code'),)


class WpIclLocaleMap(models.Model):
    code = models.CharField(max_length=7)
    locale = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_locale_map'
        unique_together = (('code', 'locale'),)


class WpIclMessageStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField(unique=True)
    object_id = models.BigIntegerField()
    from_language = models.CharField(max_length=10)
    to_language = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    md5 = models.CharField(max_length=32)
    object_type = models.CharField(max_length=64)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_message_status'


class WpIclMoFilesDomains(models.Model):
    file_path = models.CharField(max_length=250)
    file_path_md5 = models.CharField(unique=True, max_length=32)
    domain = models.CharField(max_length=45)
    status = models.CharField(max_length=20)
    num_of_strings = models.IntegerField()
    last_modified = models.IntegerField()
    component_type = models.CharField(max_length=6)
    component_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_mo_files_domains'


class WpIclNode(models.Model):
    nid = models.BigIntegerField(primary_key=True)
    md5 = models.CharField(max_length=32)
    links_fixed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_node'


class WpIclReminders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    message = models.TextField()
    url = models.TextField()
    can_delete = models.IntegerField()
    show = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_reminders'


class WpIclStringPackages(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kind_slug = models.CharField(max_length=160)
    kind = models.CharField(max_length=160)
    name = models.CharField(max_length=160)
    title = models.CharField(max_length=160)
    edit_link = models.TextField()
    view_link = models.TextField()
    post_id = models.IntegerField(blank=True, null=True)
    word_count = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_string_packages'


class WpIclStringPages(models.Model):
    id = models.BigAutoField(primary_key=True)
    string_id = models.BigIntegerField()
    url_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_string_pages'


class WpIclStringPositions(models.Model):
    id = models.BigAutoField(primary_key=True)
    string_id = models.BigIntegerField()
    kind = models.IntegerField(blank=True, null=True)
    position_in_page = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_icl_string_positions'


class WpIclStringStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField()
    string_translation_id = models.BigIntegerField()
    timestamp = models.DateTimeField()
    md5 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'wp_icl_string_status'


class WpIclStringTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    string_id = models.BigIntegerField()
    language = models.CharField(max_length=10)
    status = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    mo_string = models.TextField(blank=True, null=True)
    translator_id = models.BigIntegerField(blank=True, null=True)
    translation_service = models.CharField(max_length=16)
    batch_id = models.IntegerField()
    translation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_icl_string_translations'
        unique_together = (('string_id', 'language'),)


class WpIclStringUrls(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=7, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_string_urls'
        unique_together = (('language', 'url'),)


class WpIclStrings(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=7)
    context = models.CharField(max_length=160, blank=True, null=True)
    name = models.CharField(max_length=160, blank=True, null=True)
    value = models.TextField()
    string_package_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=40)
    title = models.CharField(max_length=160, blank=True, null=True)
    status = models.IntegerField()
    gettext_context = models.TextField()
    domain_name_context_md5 = models.CharField(unique=True, max_length=32, blank=True, null=True)
    location = models.BigIntegerField(blank=True, null=True)
    word_count = models.PositiveIntegerField(blank=True, null=True)
    translation_priority = models.CharField(max_length=160)

    class Meta:
        managed = False
        db_table = 'wp_icl_strings'


class WpIclTranslate(models.Model):
    tid = models.BigAutoField(primary_key=True)
    job_id = models.BigIntegerField()
    content_id = models.BigIntegerField()
    timestamp = models.DateTimeField()
    field_type = models.CharField(max_length=160)
    field_format = models.CharField(max_length=16)
    field_translate = models.IntegerField()
    field_data = models.TextField()
    field_data_translated = models.TextField()
    field_finished = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_translate'


class WpIclTranslateJob(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField()
    translator_id = models.PositiveIntegerField()
    translated = models.PositiveIntegerField()
    manager_id = models.PositiveIntegerField()
    revision = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=160, blank=True, null=True)
    deadline_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_translate_job'


class WpIclTranslationBatches(models.Model):
    batch_name = models.TextField()
    tp_id = models.IntegerField(blank=True, null=True)
    ts_url = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_translation_batches'


class WpIclTranslationStatus(models.Model):
    rid = models.BigAutoField(primary_key=True)
    translation_id = models.BigIntegerField(unique=True)
    status = models.IntegerField()
    translator_id = models.BigIntegerField()
    needs_update = models.IntegerField()
    md5 = models.CharField(max_length=32)
    translation_service = models.CharField(max_length=16)
    batch_id = models.IntegerField()
    translation_package = models.TextField()
    timestamp = models.DateTimeField()
    links_fixed = models.IntegerField()
    field_prevstate = models.TextField(db_column='_prevstate', blank=True, null=True)  # Field renamed because it started with '_'.
    uuid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_translation_status'


class WpIclTranslations(models.Model):
    translation_id = models.BigAutoField(primary_key=True)
    element_type = models.CharField(max_length=60)
    element_id = models.BigIntegerField(blank=True, null=True)
    trid = models.BigIntegerField()
    language_code = models.CharField(max_length=7)
    source_language_code = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_translations'
        unique_together = (('trid', 'language_code'), ('element_type', 'element_id'),)


class WpLinks(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_links'


class WpMailchimpCarts(models.Model):
    id = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True, null=True)
    cart = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_mailchimp_carts'


class WpNf3ActionMeta(models.Model):
    id = models.AutoField(unique=True)
    parent_id = models.IntegerField()
    key = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_action_meta'


class WpNf3Actions(models.Model):
    id = models.AutoField(unique=True)
    title = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_actions'


class WpNf3FieldMeta(models.Model):
    id = models.AutoField(unique=True)
    parent_id = models.IntegerField()
    key = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_field_meta'


class WpNf3Fields(models.Model):
    id = models.AutoField(unique=True)
    label = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    parent_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_fields'


class WpNf3FormMeta(models.Model):
    id = models.AutoField(unique=True)
    parent_id = models.IntegerField()
    key = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_form_meta'


class WpNf3Forms(models.Model):
    id = models.AutoField(unique=True)
    title = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    subs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_forms'


class WpNf3ObjectMeta(models.Model):
    id = models.AutoField(unique=True)
    parent_id = models.IntegerField()
    key = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_object_meta'


class WpNf3Objects(models.Model):
    id = models.AutoField(unique=True)
    type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_objects'


class WpNf3Relationships(models.Model):
    id = models.AutoField(unique=True)
    child_id = models.IntegerField()
    child_type = models.TextField()
    parent_id = models.IntegerField()
    parent_type = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_relationships'


class WpNhLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    blog_id = models.BigIntegerField()
    location_slug = models.CharField(max_length=200)
    location_name = models.TextField()
    location_owner = models.BigIntegerField()
    location_address = models.CharField(max_length=200)
    location_town = models.CharField(max_length=200)
    location_state = models.CharField(max_length=200)
    location_postcode = models.CharField(max_length=10)
    location_region = models.CharField(max_length=200)
    location_country = models.CharField(max_length=2)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    post_content = models.TextField()
    location_status = models.IntegerField()
    location_private = models.IntegerField()
    location_stamp = models.DateTimeField()
    location_update_stamp = models.DateTimeField()
    location_pintype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'wp_nh_locations'


class WpOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_options'


class WpPeepsoActivities(models.Model):
    act_id = models.BigAutoField(primary_key=True)
    act_owner_id = models.BigIntegerField()
    act_external_id = models.PositiveIntegerField(blank=True, null=True)
    act_module_id = models.PositiveSmallIntegerField()
    act_ip = models.CharField(max_length=64)
    act_access = models.PositiveIntegerField()
    act_has_replies = models.PositiveIntegerField()
    act_location_id = models.PositiveIntegerField()
    act_repost_id = models.PositiveIntegerField()
    act_link = models.CharField(max_length=100, blank=True, null=True)
    act_link_title = models.CharField(max_length=100, blank=True, null=True)
    act_link_image_id = models.PositiveIntegerField()
    act_description = models.TextField(blank=True, null=True)
    act_comment_object_id = models.BigIntegerField()
    act_comment_module_id = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_peepso_activities'


class WpPeepsoActivityHide(models.Model):
    hide_activity_id = models.BigIntegerField()
    hide_user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_peepso_activity_hide'
        unique_together = (('hide_activity_id', 'hide_user_id'),)


class WpPeepsoBlocks(models.Model):
    blk_user_id = models.BigIntegerField()
    blk_blocked_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_peepso_blocks'
        unique_together = (('blk_user_id', 'blk_blocked_id'),)


class WpPeepsoCache(models.Model):
    user_id = models.BigIntegerField()
    tables = models.CharField(max_length=200)
    query_name = models.CharField(max_length=32)
    query = models.CharField(max_length=255)
    query_hash = models.CharField(max_length=32)
    data = models.TextField()
    expires = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_peepso_cache'


class WpPeepsoErrors(models.Model):
    err_id = models.AutoField(primary_key=True)
    err_type = models.CharField(max_length=16)
    err_extra = models.CharField(max_length=32)
    err_file = models.CharField(max_length=128)
    err_func = models.CharField(max_length=128)
    err_msg = models.CharField(max_length=255)
    err_timestamp = models.DateTimeField()
    err_user_id = models.BigIntegerField()
    err_ip = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'wp_peepso_errors'


class WpPeepsoLikes(models.Model):
    like_id = models.AutoField(primary_key=True)
    like_user_id = models.BigIntegerField()
    like_external_id = models.BigIntegerField()
    like_module_id = models.PositiveSmallIntegerField()
    like_type = models.PositiveSmallIntegerField()
    like_timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_peepso_likes'
        unique_together = (('like_user_id', 'like_module_id', 'like_external_id'),)


class WpPeepsoMailQueue(models.Model):
    mail_id = models.AutoField(primary_key=True)
    mail_user_id = models.BigIntegerField(blank=True, null=True)
    mail_created_at = models.DateTimeField()
    mail_recipient = models.CharField(max_length=128)
    mail_subject = models.CharField(max_length=200)
    mail_message = models.TextField()
    mail_status = models.IntegerField()
    mail_attempts = models.IntegerField()
    mail_module_id = models.PositiveSmallIntegerField(blank=True, null=True)
    mail_message_id = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_peepso_mail_queue'


class WpPeepsoNotifications(models.Model):
    not_id = models.AutoField(primary_key=True)
    not_user_id = models.BigIntegerField()
    not_from_user_id = models.BigIntegerField()
    not_timestamp = models.DateTimeField()
    not_module_id = models.PositiveSmallIntegerField()
    not_external_id = models.BigIntegerField()
    not_type = models.CharField(max_length=20)
    not_message = models.CharField(max_length=200)
    not_read = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_peepso_notifications'


class WpPeepsoReport(models.Model):
    rep_id = models.AutoField(primary_key=True)
    rep_user_id = models.BigIntegerField()
    rep_external_id = models.BigIntegerField()
    rep_timestamp = models.DateTimeField()
    rep_reason = models.CharField(max_length=128, blank=True, null=True)
    rep_module_id = models.PositiveSmallIntegerField()
    rep_status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_peepso_report'


class WpPeepsoUnfollow(models.Model):
    unf_user_id = models.BigIntegerField()
    unf_unfollowed_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_peepso_unfollow'
        unique_together = (('unf_user_id', 'unf_unfollowed_id'),)


class WpPeepsoUsers(models.Model):
    usr_id = models.BigIntegerField(primary_key=True)
    usr_last_activity = models.DateTimeField()
    usr_views = models.PositiveIntegerField()
    usr_likes = models.PositiveIntegerField()
    usr_role = models.CharField(max_length=9, blank=True, null=True)
    usr_send_emails = models.IntegerField()
    usr_cover_photo = models.CharField(max_length=255, blank=True, null=True)
    usr_avatar_custom = models.IntegerField()
    usr_profile_acc = models.IntegerField()
    usr_first_name_acc = models.IntegerField()
    usr_last_name_acc = models.IntegerField()
    usr_description_acc = models.IntegerField()
    usr_user_url_acc = models.IntegerField()
    usr_gender = models.CharField(max_length=1, blank=True, null=True)
    usr_gender_acc = models.IntegerField()
    usr_birthdate = models.DateField(blank=True, null=True)
    usr_birthdate_acc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_peepso_users'


class WpPlugmatterAbStats(models.Model):
    id = models.AutoField(unique=True)
    date = models.DateField()
    ab_id = models.IntegerField()
    a_imp = models.IntegerField(blank=True, null=True)
    b_imp = models.IntegerField(blank=True, null=True)
    a_conv = models.IntegerField(blank=True, null=True)
    b_conv = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_plugmatter_ab_stats'


class WpPlugmatterAbTest(models.Model):
    id = models.AutoField(unique=True)
    compaign_name = models.CharField(max_length=80)
    boxa = models.CharField(db_column='boxA', max_length=80)  # Field name made lowercase.
    boxb = models.CharField(db_column='boxB', max_length=100, blank=True, null=True)  # Field name made lowercase.
    home = models.CharField(max_length=8, blank=True, null=True)
    page = models.CharField(max_length=8, blank=True, null=True)
    post = models.CharField(max_length=8, blank=True, null=True)
    archieve = models.CharField(max_length=8, blank=True, null=True)
    start_date = models.CharField(max_length=80)
    active = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_plugmatter_ab_test'


class WpPlugmatterTemplates(models.Model):
    id = models.AutoField(unique=True)
    temp_name = models.CharField(max_length=80)
    base_temp_name = models.CharField(max_length=80)
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_plugmatter_templates'


class WpPmxiFiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    import_id = models.BigIntegerField()
    name = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    registered_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_pmxi_files'


class WpPmxiHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    import_id = models.BigIntegerField()
    type = models.CharField(max_length=10)
    time_run = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    summary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_pmxi_history'


class WpPmxiImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    attachment_id = models.BigIntegerField()
    image_url = models.CharField(max_length=600)
    image_filename = models.CharField(max_length=600)

    class Meta:
        managed = False
        db_table = 'wp_pmxi_images'


class WpPmxiImports(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_import_id = models.BigIntegerField()
    name = models.TextField(blank=True, null=True)
    friendly_name = models.CharField(max_length=255)
    type = models.CharField(max_length=32)
    feed_type = models.CharField(max_length=3)
    path = models.TextField(blank=True, null=True)
    xpath = models.TextField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)
    registered_on = models.DateTimeField()
    root_element = models.CharField(max_length=255, blank=True, null=True)
    processing = models.IntegerField()
    executing = models.IntegerField()
    triggered = models.IntegerField()
    queue_chunk_number = models.BigIntegerField()
    first_import = models.DateTimeField()
    count = models.BigIntegerField()
    imported = models.BigIntegerField()
    created = models.BigIntegerField()
    updated = models.BigIntegerField()
    skipped = models.BigIntegerField()
    deleted = models.BigIntegerField()
    canceled = models.IntegerField()
    canceled_on = models.DateTimeField()
    failed = models.IntegerField()
    failed_on = models.DateTimeField()
    settings_update_on = models.DateTimeField()
    last_activity = models.DateTimeField()
    iteration = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_pmxi_imports'


class WpPmxiPosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    import_id = models.BigIntegerField()
    unique_key = models.TextField(blank=True, null=True)
    product_key = models.TextField(blank=True, null=True)
    iteration = models.BigIntegerField()
    specified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_pmxi_posts'


class WpPmxiTemplates(models.Model):
    id = models.BigAutoField(primary_key=True)
    options = models.TextField(blank=True, null=True)
    scheduled = models.CharField(max_length=64)
    name = models.CharField(max_length=200)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    is_keep_linebreaks = models.IntegerField()
    is_leave_html = models.IntegerField()
    fix_characters = models.IntegerField()
    meta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_pmxi_templates'


class WpPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_postmeta'


class WpPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_posts'


class WpPwGcmusers(models.Model):
    gcm_regid = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)
    device = models.CharField(max_length=128, blank=True, null=True)
    topics = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_pw_gcmusers'


class WpQueue(models.Model):
    id = models.BigAutoField(primary_key=True)
    job = models.TextField()
    attempts = models.IntegerField()
    locked = models.IntegerField()
    locked_at = models.DateTimeField(blank=True, null=True)
    available_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_queue'


class WpRevsliderCss(models.Model):
    id = models.AutoField(unique=True)
    handle = models.TextField()
    settings = models.TextField(blank=True, null=True)
    hover = models.TextField(blank=True, null=True)
    params = models.TextField()
    advanced = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_revslider_css'


class WpRevsliderLayerAnimations(models.Model):
    id = models.AutoField(unique=True)
    handle = models.TextField()
    params = models.TextField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_revslider_layer_animations'


class WpRevsliderNavigations(models.Model):
    id = models.AutoField(unique=True)
    name = models.CharField(max_length=191)
    handle = models.CharField(max_length=191)
    css = models.TextField()
    markup = models.TextField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_revslider_navigations'


class WpRevsliderSliders(models.Model):
    id = models.AutoField(unique=True)
    title = models.TextField()
    alias = models.TextField(blank=True, null=True)
    params = models.TextField()
    settings = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'wp_revslider_sliders'


class WpRevsliderSlides(models.Model):
    id = models.AutoField(unique=True)
    slider_id = models.IntegerField()
    slide_order = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_revslider_slides'


class WpRevsliderStaticSlides(models.Model):
    id = models.AutoField(unique=True)
    slider_id = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_revslider_static_slides'


class WpScrollNews(models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=2000)
    createdon = models.DateTimeField()
    custom_link = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_scroll_news'


class WpScsOcto(models.Model):
    pid = models.IntegerField()
    unique_id = models.CharField(max_length=8)
    label = models.CharField(max_length=128)
    active = models.IntegerField()
    original_id = models.IntegerField()
    is_base = models.IntegerField()
    img = models.CharField(max_length=64)
    sort_order = models.IntegerField()
    params = models.TextField()
    is_pro = models.IntegerField()
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_scs_octo'


class WpScsOctoBlocks(models.Model):
    oid = models.IntegerField()
    cid = models.IntegerField()
    unique_id = models.CharField(max_length=8)
    label = models.CharField(max_length=128)
    original_id = models.IntegerField()
    params = models.TextField()
    html = models.TextField()
    css = models.TextField()
    img = models.CharField(max_length=64, blank=True, null=True)
    sort_order = models.IntegerField()
    is_base = models.IntegerField()
    is_pro = models.IntegerField()
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_scs_octo_blocks'


class WpScsOctoBlocksCategories(models.Model):
    code = models.CharField(max_length=32)
    label = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'wp_scs_octo_blocks_categories'


class WpScsSubscribers(models.Model):
    username = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128)
    hash = models.CharField(max_length=128)
    activated = models.IntegerField()
    block_id = models.IntegerField()
    date_created = models.DateTimeField()
    all_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_scs_subscribers'


class WpSmushDirImages(models.Model):
    id = models.AutoField(unique=True)
    path = models.TextField()
    resize = models.CharField(max_length=55, blank=True, null=True)
    lossy = models.CharField(max_length=55, blank=True, null=True)
    error = models.CharField(max_length=55, blank=True, null=True)
    image_size = models.PositiveIntegerField(blank=True, null=True)
    orig_size = models.PositiveIntegerField(blank=True, null=True)
    file_time = models.PositiveIntegerField(blank=True, null=True)
    last_scan = models.DateTimeField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    path_hash = models.CharField(unique=True, max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_smush_dir_images'


class WpSpDsgvoLogs(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    log_date = models.DateTimeField()
    log_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_sp_dsgvo_logs'


class WpTermRelationships(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'),)


class WpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)


class WpTermmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    term_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_termmeta'


class WpTerms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_terms'


class WpUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_usermeta'


class WpUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'wp_users'


class WpWapNexForms(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    plugin = models.CharField(max_length=255, blank=True, null=True)
    publish = models.PositiveIntegerField(blank=True, null=True)
    added = models.CharField(max_length=18, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mail_to = models.TextField(blank=True, null=True)
    confirmation_mail_body = models.TextField(blank=True, null=True)
    admin_email_body = models.TextField(blank=True, null=True)
    confirmation_mail_subject = models.TextField(blank=True, null=True)
    user_confirmation_mail_subject = models.TextField(blank=True, null=True)
    from_address = models.TextField(blank=True, null=True)
    from_name = models.TextField(blank=True, null=True)
    on_screen_confirmation_message = models.TextField(blank=True, null=True)
    confirmation_page = models.TextField(blank=True, null=True)
    form_fields = models.TextField(blank=True, null=True)
    clean_html = models.TextField(blank=True, null=True)
    visual_settings = models.TextField(blank=True, null=True)
    google_analytics_conversion_code = models.TextField(blank=True, null=True)
    colour_scheme = models.TextField(blank=True, null=True)
    send_user_mail = models.TextField(blank=True, null=True)
    user_email_field = models.TextField(blank=True, null=True)
    on_form_submission = models.TextField(blank=True, null=True)
    date_sent = models.DateTimeField(blank=True, null=True)
    is_form = models.TextField(blank=True, null=True)
    is_template = models.TextField(blank=True, null=True)
    hidden_fields = models.TextField(blank=True, null=True)
    custom_url = models.TextField(blank=True, null=True)
    post_type = models.TextField(blank=True, null=True)
    post_action = models.TextField(blank=True, null=True)
    bcc = models.TextField(blank=True, null=True)
    bcc_user_mail = models.TextField(blank=True, null=True)
    custom_css = models.TextField(blank=True, null=True)
    is_paypal = models.TextField(blank=True, null=True)
    total_views = models.TextField(blank=True, null=True)
    time_viewed = models.TextField(blank=True, null=True)
    email_on_payment_success = models.TextField(blank=True, null=True)
    conditional_logic = models.TextField(blank=True, null=True)
    server_side_logic = models.TextField(blank=True, null=True)
    form_status = models.TextField(blank=True, null=True)
    currency_code = models.TextField(blank=True, null=True)
    products = models.TextField(blank=True, null=True)
    business = models.TextField(blank=True, null=True)
    cmd = models.TextField(blank=True, null=True)
    return_url = models.TextField(blank=True, null=True)
    cancel_url = models.TextField(blank=True, null=True)
    lc = models.TextField(blank=True, null=True)
    environment = models.TextField(blank=True, null=True)
    form_type = models.TextField(blank=True, null=True)
    template_type = models.TextField(blank=True, null=True)
    draft_id = models.TextField(db_column='draft_Id', blank=True, null=True)  # Field name made lowercase.
    email_subscription = models.TextField(blank=True, null=True)
    mc_field_map = models.TextField(blank=True, null=True)
    mc_list_id = models.TextField(blank=True, null=True)
    gr_field_map = models.TextField(blank=True, null=True)
    gr_list_id = models.TextField(blank=True, null=True)
    conditional_logic_array = models.TextField(blank=True, null=True)
    pdf_html = models.TextField(blank=True, null=True)
    attach_pdf_to_email = models.TextField(blank=True, null=True)
    form_to_post_map = models.TextField(blank=True, null=True)
    is_form_to_post = models.TextField(blank=True, null=True)
    form_hidden_fields = models.TextField(blank=True, null=True)
    jq_theme = models.TextField(blank=True, null=True)
    md_theme = models.TextField(blank=True, null=True)
    form_theme = models.TextField(blank=True, null=True)
    form_style = models.TextField(blank=True, null=True)
    is_wrapped = models.TextField(blank=True, null=True)
    multistep_settings = models.TextField(blank=True, null=True)
    multistep_html = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wap_nex_forms'


class WpWapNexFormsEmailTemplates(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    plugin = models.CharField(max_length=255, blank=True, null=True)
    publish = models.PositiveIntegerField(blank=True, null=True)
    added = models.CharField(max_length=18, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    nex_forms_id = models.TextField(db_column='nex_forms_Id', blank=True, null=True)  # Field name made lowercase.
    mail_type = models.TextField(blank=True, null=True)
    mail_to = models.TextField(blank=True, null=True)
    mail_body = models.TextField(blank=True, null=True)
    mail_subject = models.TextField(blank=True, null=True)
    from_address = models.TextField(blank=True, null=True)
    from_name = models.TextField(blank=True, null=True)
    send_user_mail = models.TextField(blank=True, null=True)
    user_email_field = models.TextField(blank=True, null=True)
    bcc = models.TextField(blank=True, null=True)
    bcc_user_mail = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wap_nex_forms_email_templates'


class WpWapNexFormsEntries(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    plugin = models.CharField(max_length=255, blank=True, null=True)
    publish = models.PositiveIntegerField(blank=True, null=True)
    added = models.CharField(max_length=18, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    nex_forms_id = models.TextField(db_column='nex_forms_Id', blank=True, null=True)  # Field name made lowercase.
    page = models.TextField(blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    user_id = models.TextField(db_column='user_Id', blank=True, null=True)  # Field name made lowercase.
    viewed = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    paypal_invoice = models.TextField(blank=True, null=True)
    payment_status = models.TextField(blank=True, null=True)
    form_data = models.TextField(blank=True, null=True)
    paypal_data = models.TextField(blank=True, null=True)
    hostname = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    loc = models.TextField(blank=True, null=True)
    org = models.TextField(blank=True, null=True)
    postal = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wap_nex_forms_entries'


class WpWapNexFormsFiles(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    plugin = models.CharField(max_length=255, blank=True, null=True)
    publish = models.PositiveIntegerField(blank=True, null=True)
    added = models.CharField(max_length=18, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    nex_forms_id = models.TextField(db_column='nex_forms_Id', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    entry_id = models.TextField(db_column='entry_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wap_nex_forms_files'


class WpWapNexFormsStats(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    plugin = models.CharField(max_length=255, blank=True, null=True)
    publish = models.PositiveIntegerField(blank=True, null=True)
    added = models.CharField(max_length=18, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    nex_forms_id = models.TextField(db_column='nex_forms_Id', blank=True, null=True)  # Field name made lowercase.
    time_viewed = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wap_nex_forms_stats'


class WpWapNexFormsStatsInteractions(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    plugin = models.CharField(max_length=255, blank=True, null=True)
    publish = models.PositiveIntegerField(blank=True, null=True)
    added = models.CharField(max_length=18, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    nex_forms_id = models.TextField(db_column='nex_forms_Id', blank=True, null=True)  # Field name made lowercase.
    time_interacted = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wap_nex_forms_stats_interactions'


class WpWapNexFormsTempReport(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entry_id = models.TextField(blank=True, null=True)
    nombres = models.TextField(blank=True, null=True)
    apellidos = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    telefon = models.TextField(blank=True, null=True)
    tienes_algn_plan_que_quieras_reservar_field = models.TextField(db_column='tienes_algn_plan_que_quieras_reservar_', blank=True, null=True)  # Field renamed because it ended with '_'.
    que_buscas = models.TextField(blank=True, null=True)
    opciones_de_viaje = models.TextField(blank=True, null=True)
    alimentacin = models.TextField(blank=True, null=True)
    opciones_de_pago = models.TextField(blank=True, null=True)
    cual_es_tu_monto_reservado = models.TextField(blank=True, null=True)
    movilidad = models.TextField(blank=True, null=True)
    cantidad_de_personas_adultas_que_viajan = models.TextField(blank=True, null=True)
    hay_personas_con_incapacidad_fisica = models.TextField(blank=True, null=True)
    llevas_el_coche_de_bebe = models.TextField(blank=True, null=True)
    saliendo_desde = models.TextField(blank=True, null=True)
    llegando_a = models.TextField(blank=True, null=True)
    fecha_de_salida = models.TextField(blank=True, null=True)
    fecha_de_regreso = models.TextField(blank=True, null=True)
    deseaas_un_seguro_de_viaje_si_no = models.TextField(db_column='deseaas_un_seguro_de_viaje_si__no', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    deseas_un_taxi_a_el_aeropuerto = models.TextField(blank=True, null=True)
    algo_extra_que_deseas_comentarnos_field = models.TextField(db_column='algo_extra_que_deseas_comentarnos_', blank=True, null=True)  # Field renamed because it ended with '_'.
    radio_buttons = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wap_nex_forms_temp_report'


class WpWapNexFormsViews(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    plugin = models.CharField(max_length=255, blank=True, null=True)
    publish = models.PositiveIntegerField(blank=True, null=True)
    added = models.CharField(max_length=18, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    nex_forms_id = models.TextField(db_column='nex_forms_Id', blank=True, null=True)  # Field name made lowercase.
    time_viewed = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wap_nex_forms_views'


class WpWcDownloadLog(models.Model):
    download_log_id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    permission = models.ForeignKey('WpWoocommerceDownloadableProductPermissions', models.DO_NOTHING)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_download_log'


class WpWcWebhooks(models.Model):
    webhook_id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=200)
    name = models.TextField()
    user_id = models.BigIntegerField()
    delivery_url = models.TextField()
    secret = models.TextField()
    topic = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_modified_gmt = models.DateTimeField()
    api_version = models.SmallIntegerField()
    failure_count = models.SmallIntegerField()
    pending_delivery = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_webhooks'


class WpWoocommerceApiKeys(models.Model):
    key_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    description = models.CharField(max_length=200, blank=True, null=True)
    permissions = models.CharField(max_length=10)
    consumer_key = models.CharField(max_length=64)
    consumer_secret = models.CharField(max_length=43)
    nonces = models.TextField(blank=True, null=True)
    truncated_key = models.CharField(max_length=7)
    last_access = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_api_keys'


class WpWoocommerceAttributeTaxonomies(models.Model):
    attribute_id = models.BigAutoField(primary_key=True)
    attribute_name = models.CharField(max_length=200)
    attribute_label = models.CharField(max_length=200, blank=True, null=True)
    attribute_type = models.CharField(max_length=20)
    attribute_orderby = models.CharField(max_length=20)
    attribute_public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_attribute_taxonomies'


class WpWoocommerceDownloadableProductPermissions(models.Model):
    permission_id = models.BigAutoField(primary_key=True)
    download_id = models.CharField(max_length=36)
    product_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    order_key = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_id = models.BigIntegerField(blank=True, null=True)
    downloads_remaining = models.CharField(max_length=9, blank=True, null=True)
    access_granted = models.DateTimeField()
    access_expires = models.DateTimeField(blank=True, null=True)
    download_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_downloadable_product_permissions'


class WpWoocommerceLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    level = models.SmallIntegerField()
    source = models.CharField(max_length=200)
    message = models.TextField()
    context = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_log'


class WpWoocommerceOrderItemmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    order_item_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_order_itemmeta'


class WpWoocommerceOrderItems(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    order_item_name = models.TextField()
    order_item_type = models.CharField(max_length=200)
    order_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_order_items'


class WpWoocommercePaymentTokenmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    payment_token_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_payment_tokenmeta'


class WpWoocommercePaymentTokens(models.Model):
    token_id = models.BigAutoField(primary_key=True)
    gateway_id = models.CharField(max_length=200)
    token = models.TextField()
    user_id = models.BigIntegerField()
    type = models.CharField(max_length=200)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_payment_tokens'


class WpWoocommerceSessions(models.Model):
    session_id = models.BigAutoField(primary_key=True)
    session_key = models.CharField(unique=True, max_length=32)
    session_value = models.TextField()
    session_expiry = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_sessions'


class WpWoocommerceShippingZoneLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    zone_id = models.BigIntegerField()
    location_code = models.CharField(max_length=200)
    location_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zone_locations'


class WpWoocommerceShippingZoneMethods(models.Model):
    zone_id = models.BigIntegerField()
    instance_id = models.BigAutoField(primary_key=True)
    method_id = models.CharField(max_length=200)
    method_order = models.BigIntegerField()
    is_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zone_methods'


class WpWoocommerceShippingZones(models.Model):
    zone_id = models.BigAutoField(primary_key=True)
    zone_name = models.CharField(max_length=200)
    zone_order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zones'


class WpWoocommerceTaxRateLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    location_code = models.CharField(max_length=200)
    tax_rate_id = models.BigIntegerField()
    location_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_tax_rate_locations'


class WpWoocommerceTaxRates(models.Model):
    tax_rate_id = models.BigAutoField(primary_key=True)
    tax_rate_country = models.CharField(max_length=2)
    tax_rate_state = models.CharField(max_length=200)
    tax_rate = models.CharField(max_length=8)
    tax_rate_name = models.CharField(max_length=200)
    tax_rate_priority = models.BigIntegerField()
    tax_rate_compound = models.IntegerField()
    tax_rate_shipping = models.IntegerField()
    tax_rate_order = models.BigIntegerField()
    tax_rate_class = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_tax_rates'


class WpWpbackitupJobControl(models.Model):
    job_id = models.BigIntegerField(primary_key=True)
    job_type = models.CharField(max_length=45)
    job_run_type = models.CharField(max_length=45)
    job_name = models.CharField(max_length=100)
    job_meta = models.TextField(blank=True, null=True)
    job_start = models.DateTimeField(blank=True, null=True)
    job_end = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    job_status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'wp_wpbackitup_job_control'


class WpWpbackitupJobItems(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    job_id = models.BigIntegerField()
    batch_id = models.BigIntegerField(blank=True, null=True)
    group_id = models.CharField(max_length=15, blank=True, null=True)
    item = models.TextField(blank=True, null=True)
    size_kb = models.BigIntegerField(blank=True, null=True)
    retry_count = models.IntegerField()
    offset = models.BigIntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    record_type = models.CharField(max_length=1)
    item_status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'wp_wpbackitup_job_items'


class WpWpbackitupJobTasks(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    job_id = models.BigIntegerField()
    task_name = models.CharField(max_length=45)
    task_meta = models.TextField(blank=True, null=True)
    task_start = models.DateTimeField(blank=True, null=True)
    task_end = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    allocation_id = models.BigIntegerField(blank=True, null=True)
    retry_count = models.IntegerField()
    error = models.IntegerField()
    task_status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'wp_wpbackitup_job_tasks'


class WpWsluserscontacts(models.Model):
    id = models.AutoField(unique=True)
    user_id = models.IntegerField()
    provider = models.CharField(max_length=50)
    identifier = models.CharField(max_length=255)
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=255)
    profile_url = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_wsluserscontacts'


class WpWslusersprofiles(models.Model):
    id = models.AutoField(unique=True)
    user_id = models.IntegerField()
    provider = models.CharField(max_length=50)
    object_sha = models.CharField(max_length=45)
    identifier = models.CharField(max_length=255)
    profileurl = models.CharField(max_length=255)
    websiteurl = models.CharField(max_length=255)
    photourl = models.CharField(max_length=255)
    displayname = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    language = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    birthday = models.IntegerField()
    birthmonth = models.IntegerField()
    birthyear = models.IntegerField()
    email = models.CharField(max_length=255)
    emailverified = models.CharField(max_length=255)
    phone = models.CharField(max_length=75)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=75)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'wp_wslusersprofiles'
