# Generated by Django 3.0.2 on 2020-01-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zamienniki', '0006_auto_20200115_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zamiennik',
            name='liczbaECTS',
            field=models.PositiveSmallIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='zamiennik',
            name='liczbaGodzin',
            field=models.PositiveSmallIntegerField(default=30),
            preserve_default=False,
        ),
    ]
