# Generated by Django 2.2.4 on 2019-08-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp_up', '0003_auto_20190811_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grasshopper',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]