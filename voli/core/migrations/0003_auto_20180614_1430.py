# Generated by Django 2.0.6 on 2018-06-14 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180613_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='origin_url',
            field=models.CharField(default='no url', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
