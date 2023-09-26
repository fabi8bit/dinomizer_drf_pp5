from rest_framework import generics, permissions, filters
from dm_drf_api.permissions import IsOwnerOrReadOnly
from .models import Asset
from .serializers import AssetSerializer
from rest_framework.permissions import IsAuthenticated


class AssetList(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'owner__username',
        'asset_name',
        'category'
        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]
    queryset = Asset.objects.all()