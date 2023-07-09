# Generated by Django 3.2.20 on 2023-07-09 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='product',
            name='brands',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='product',
            name='packaging',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(max_length=550),
        ),
    ]
