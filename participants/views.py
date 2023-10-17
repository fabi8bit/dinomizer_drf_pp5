from rest_framework import generics, permissions, filters
from dm_drf_api.permissions import IsOwnerOrReadOnly
from .models import Participant
from .serializers import ParticipantSerializer
from rest_framework.permissions import IsAuthenticated


class ParticipantList(generics.ListCreateAPIView):
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly
    # ]
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'project_id__id',
        ]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ParticipantDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()