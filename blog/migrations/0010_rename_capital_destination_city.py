# Generated by Django 3.2.7 on 2021-09-21 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210921_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='capital',
            new_name='city',
        ),
    ]
