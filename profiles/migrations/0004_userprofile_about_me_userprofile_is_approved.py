# Generated by Django 4.2.11 on 2024-04-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_neurodiversity_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about_me',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]