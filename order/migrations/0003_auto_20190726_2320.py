# Generated by Django 2.1.5 on 2019-07-26 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_details', '0001_initial'),
        ('order', '0002_auto_20190726_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_details',
        ),
        migrations.AddField(
            model_name='order',
            name='order_details',
            field=models.ManyToManyField(to='order_details.OrderDetail'),
        ),
    ]
