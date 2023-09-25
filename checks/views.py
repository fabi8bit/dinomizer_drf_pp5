from rest_framework import generics, permissions
from dm_drf_api.permissions import IsOwnerOrReadOnly, IsProjectOwner
from .models import Check
from .serializers import CheckSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from assets.models import Asset
from projects.models import Project


# class CheckList(generics.ListCreateAPIView):
#     permission_classes = [IsProjectOwner]
#     serializer_class = CheckSerializer
#     queryset = Check.objects.all()

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

class CheckList(APIView):
    serializer_class = CheckSerializer
    permission_classes = [IsAuthenticated & IsProjectOwner]

    def get(self, request):
        checks = Check.objects.all()
        serializer = CheckSerializer(
            checks, many=True, context={'request':request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = CheckSerializer(
            data=request.data, context={'request':request}
        )
        if serializer.is_valid():
            asset_id = request.data['asset_id']
            asset = Asset.objects.get(pk=asset_id)
            if asset.project_id.owner == request.user:
                serializer.save(owner=request.user)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    serializer.errors, status=status.HTTP_403_FORBIDDEN
                    )
        return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        

class CheckDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsProjectOwner]
    serializer_class = CheckSerializer
    queryset = Check.objects.all()