# Generated by Django 4.2 on 2023-04-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
