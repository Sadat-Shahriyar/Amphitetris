# Generated by Django 2.2.5 on 2020-09-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_auto_20200920_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='product_description',
            field=models.CharField(default='', max_length=650),
        ),
    ]
