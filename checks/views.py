from rest_framework import generics, permissions
from dm_drf_api.permissions import IsOwnerOrReadOnly, IsProjectOwner
from .models import Check
from .serializers import CheckSerializer
from rest_framework.permissions import IsAuthenticated

class CheckList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated & IsProjectOwner]
    serializer_class = CheckSerializer
    queryset = Check.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CheckDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsProjectOwner]
    serializer_class = CheckSerializer
    queryset = Check.objects.all()