# Generated by Django 2.1.5 on 2019-02-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='FishSauce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.FloatField()),
                ('produce_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('quanity', models.IntegerField()),
                ('image', models.ImageField(upload_to='uploads/')),
                ('type_product', models.IntegerField(default=1)),
                ('volume', models.FloatField(default=0)),
                ('protein', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'fishsauce',
            },
        ),
    ]
