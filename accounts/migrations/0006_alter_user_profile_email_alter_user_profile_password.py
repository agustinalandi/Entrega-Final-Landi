# Generated by Django 4.0.4 on 2022-07-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_profile_chosen_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='email',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
