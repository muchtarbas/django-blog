# Generated by Django 3.0 on 2020-01-03 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptography', '0006_auto_20200104_0030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='category',
        ),
    ]
