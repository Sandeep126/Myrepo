# Generated by Django 2.1.5 on 2019-06-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0005_auto_20190615_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beers',
            name='Beer_Name',
            field=models.CharField(default='Default', max_length=255),
        ),
        migrations.AlterField(
            model_name='beers_rateing',
            name='Beer_Name',
            field=models.CharField(default='Default', max_length=255),
        ),
    ]
