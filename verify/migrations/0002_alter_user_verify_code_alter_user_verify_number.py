# Generated by Django 4.2.7 on 2023-12-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_verify',
            name='code',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='user_verify',
            name='number',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
