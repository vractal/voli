# Generated by Django 2.0.6 on 2018-06-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='origin_url',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]