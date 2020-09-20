# Generated by Django 2.2.5 on 2020-09-20 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenderBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('amount', models.IntegerField()),
                ('product_description', models.CharField(max_length=650)),
                ('delivery_date', models.DateField()),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.Tender')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Profile')),
            ],
        ),
    ]
