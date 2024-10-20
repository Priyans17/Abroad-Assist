# Generated by Django 5.0.6 on 2024-09-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.TextField(max_length=40)),
                ('gen_otp', models.IntegerField(max_length=6)),
            ],
        ),
    ]
