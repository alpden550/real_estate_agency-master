# Generated by Django 2.2.4 on 2019-10-16 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20191009_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='owner_phonenumber',
        ),
    ]
