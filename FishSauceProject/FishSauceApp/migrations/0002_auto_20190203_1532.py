# Generated by Django 2.1.5 on 2019-02-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FishSauceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishsauce',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]
