# Generated by Django 5.1.1 on 2024-09-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0005_transportation_paid_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportation',
            name='cargo_owner',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Владелец груза'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='license_plate',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Госномер'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='loading_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата Погрузки'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='route',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='transport_price',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Цена перевозки'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='unloading_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата Выгрузки'),
        ),
    ]
