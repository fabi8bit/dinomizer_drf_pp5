from django.http import Http404
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer
from dm_drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


# class ProjectList(APIView):
#     serializer_class = ProjectSerializer
#     # permission_classes = [
#     #     permissions.IsAuthenticatedOrReadOnly
#     # ]

#     def get(self, request):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(
#             projects, many=True, context={'request': request}
#         )
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProjectSerializer(
#             data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'owner__username',
        'project_name',
        'content'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectDetail(APIView):
    permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]
    serializer_class = ProjectSerializer

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        projects = self.get_object(pk)
        serializer = ProjectSerializer(
            projects, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        projects = self.get_object(pk)
        serializer = ProjectSerializer(
            projects, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
