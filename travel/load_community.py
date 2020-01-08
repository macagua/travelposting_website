import csv
import os

import django
import ipdb

from config.settings import local as settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
django.setup()

from apps.accounts.models import CustomerUser

archivo = csv.reader(open('comunidad.csv'), delimiter=';')

ipdb.set_trace()

for linea in archivo:
    print(linea)
    usuario, create = CustomerUser.objects.get_or_create(
        email=linea[0],
        first_name=linea[1],
        last_name=linea[2],
        phone=linea[3],
        mobile=linea[4],
        business_address=linea[13],
        country=linea[10],
        is_active=True,
        is_community=True,
    )

    if create:
        usuario.set_password('travelposting2020')
        usuario.save()
        print(f"Usuario creado con exito. {linea[0]}")
    else:
        print(f"Usuario Ignorado..... {linea[0]}")
