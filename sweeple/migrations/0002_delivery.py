# Generated by Django 2.1.8 on 2019-08-15 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweeple', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taste', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
