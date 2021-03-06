# Generated by Django 2.1.5 on 2019-02-04 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FishSauceApp', '0002_auto_20190203_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishsauce',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishsauce',
            name='produce_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishsauce',
            name='protein',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='fishsauce',
            name='quanity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fishsauce',
            name='volume',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
