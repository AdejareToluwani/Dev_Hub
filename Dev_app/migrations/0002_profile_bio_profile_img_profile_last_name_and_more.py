# Generated by Django 4.1 on 2023-05-16 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dev_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='', upload_to='users_image'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
