# Generated by Django 2.1.5 on 2019-08-24 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_details', '0005_auto_20190824_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='discount',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
    ]
