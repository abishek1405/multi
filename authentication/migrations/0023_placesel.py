# Generated by Django 4.0.6 on 2022-08-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0022_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='placesel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.IntegerField()),
                ('name', models.CharField(max_length=120)),
                ('datee', models.CharField(max_length=14)),
                ('dep', models.CharField(max_length=100)),
                ('compdet', models.CharField(max_length=500)),
                ('annu', models.CharField(max_length=30)),
                ('fil', models.FileField(upload_to='')),
            ],
        ),
    ]
