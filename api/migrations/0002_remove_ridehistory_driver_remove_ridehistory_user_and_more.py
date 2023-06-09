# Generated by Django 4.2.1 on 2023-06-03 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ridehistory',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='ridehistory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='riderequest',
            name='additional_details',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='riderequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='riderequest',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver_rides', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='riderequest',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined'), ('COMPLETED', 'Completed')], default='PENDING', max_length=20),
        ),
        migrations.DeleteModel(
            name='DriverRating',
        ),
        migrations.DeleteModel(
            name='RideHistory',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
