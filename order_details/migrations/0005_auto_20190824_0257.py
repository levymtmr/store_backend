# Generated by Django 2.1.5 on 2019-08-24 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_details', '0004_remove_orderdetail_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5),
        ),
    ]