# Generated by Django 3.0.2 on 2020-01-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicjatorzy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inicjator',
            name='rola',
            field=models.CharField(choices=[('ST', 'Student'), ('OO', 'Osoba Opiniująca')], default='ST', max_length=20),
        ),
    ]