from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import RideRequest, RideHistory
from .serializers import RideRequestSerializer, RideHistorySerializer

class RideRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = RideRequestSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return RideRequest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RideHistoryListView(generics.ListAPIView):
    serializer_class = RideHistorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return RideHistory.objects.filter(user=self.request.user)
