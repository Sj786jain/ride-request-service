from django.db import models
from django.contrib.auth.models import User

class RideRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    additional_details = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('ACCEPTED', 'Accepted'),
            ('DECLINED', 'Declined'),
            ('COMPLETED', 'Completed')
        ],
        default='PENDING'
    )
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='driver_rides')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"RideRequest {self.id}"
