# Generated by Django 2.1.5 on 2019-06-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0004_beers_rateing'),
    ]

    operations = [
        migrations.AddField(
            model_name='beers',
            name='Beer_Name',
            field=models.CharField(default='san', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beers_rateing',
            name='Beer_Name',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]