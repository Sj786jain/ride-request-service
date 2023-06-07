from rest_framework import serializers, viewsets, permissions
from .models import RideRequest

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = '__all__'

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status='PENDING')

    def update(self, request, *args, **kwargs):
        # Check if the request user is the assigned driver and update the status
        instance = self.get_object()
        if instance.driver == request.user and 'status' in request.data:
            instance.status = request.data['status']
            instance.save()
        else:
            return super().update(request, *args, **kwargs)
