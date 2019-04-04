import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()


from myproject.bands.models import Band, Member


def csv_to_list(filename: str) -> list:
    '''
    Lê um csv e retorna um OrderedDict.

    Créditos para Rafael Henrique
    https://bit.ly/2FLDHsH
    '''
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        csv_data = [line for line in reader]
    return csv_data


def create_bands():
    bands = csv_to_list('fix/bands.csv')
    aux = []
    for band in bands:
        can_rock = True if band['can_rock'] == 'true' else False
        obj = Band(name=band['name'], can_rock=can_rock)
        aux.append(obj)
    Band.objects.bulk_create(aux)


def create_members():
    members = csv_to_list('fix/members.csv')
    aux = []
    for member in members:
        band_name = member['band']
        band = Band.objects.get(name=band_name)
        obj = Member(
            band=band,
            instrument=member['instrument'],
            name=member['name']
        )
        aux.append(obj)
    Member.objects.bulk_create(aux)


Band.objects.all().delete()
create_bands()
create_members()
