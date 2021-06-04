# Generated by Django 2.2 on 2021-06-04 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_profile', '0002_housenotifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='housenotifications',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_notification', to='login_and_profile.User'),
        ),
    ]
