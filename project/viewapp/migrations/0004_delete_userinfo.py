# Generated by Django 5.0.6 on 2024-07-30 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewapp', '0003_userinfo_address_userinfo_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
