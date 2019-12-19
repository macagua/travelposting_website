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
        is_active=True,
        is_community=True,
        password='$2a$10$8nCLD8zPSFLkYScG4Ihcde9q7YiEG5zvT8VgVr6hit3nrCQ5w/YVy',
    )

    if create:
        print(f"Usuario creado con exito. {linea[0]}")
    else:
        print(f"Usuario Ignorado..... {linea[0]}")
