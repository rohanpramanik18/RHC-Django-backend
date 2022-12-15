# Generated by Django 4.1.3 on 2022-12-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asha',
            fields=[
                ('asha_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
