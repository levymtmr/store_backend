# Generated by Django 2.1.5 on 2019-04-13 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190413_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
