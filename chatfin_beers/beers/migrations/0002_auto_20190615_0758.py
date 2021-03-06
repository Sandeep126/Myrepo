# Generated by Django 2.1.5 on 2019-06-15 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IBU', models.IntegerField()),
                ('Calories', models.IntegerField()),
                ('ABV', models.IntegerField()),
                ('Style', models.CharField(max_length=255)),
                ('BreweryLocation', models.CharField(max_length=255)),
                ('Created_User', models.CharField(max_length=255)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Puppy',
        ),
    ]
