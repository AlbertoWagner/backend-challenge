# Generated by Django 3.2.20 on 2023-07-09 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230709_0025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-imported_t']},
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.BigIntegerField(unique=True),
        ),
    ]
