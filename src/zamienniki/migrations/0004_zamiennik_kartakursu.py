# Generated by Django 3.0.2 on 2020-01-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zamienniki', '0003_auto_20200106_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='zamiennik',
            name='kartaKursu',
            field=models.CharField(default='', max_length=80),
        ),
    ]