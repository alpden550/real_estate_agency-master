# Generated by Django 2.2.4 on 2019-10-09 18:54
import phonenumbers
from django.db import migrations


def format_phones(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        user_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if not phonenumbers.is_valid_number(user_phone):
            flat.owner_phone_pure = None
            flat.save()
            continue
        flat.owner_phone_pure = user_phone
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20191009_2132'),
    ]

    operations = [
        migrations.RunPython(format_phones),
    ]
