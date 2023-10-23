from django.contrib.auth.models import User
from .models import Asset
from projects.models import Project
from rest_framework import status
from rest_framework.test import APITestCase


class AssetDetailViewTests(APITestCase):
    def setUp(self):
        admin = User.objects.create_user(username='admin', password='pass')
        fabio = User.objects.create_user(username='fabio', password='pass')
        project = Project.objects.create(
            owner=admin,
            project_name='a title',
            content='admins content'
        )

        Asset.objects.create(
            owner=fabio,
            asset_name='new asset',
            project_id=project
            )

    def test_project_owner_can_check_asset_related_to_his_project(self):
        self.client.login(username='admin', password='pass')
        response = self.client.post('/checks/', {'asset_id': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_and_NOT_project_owner_cant_check_asset(self):
        self.client.login(username='fabio', password='pass')
        response = self.client.post('/checks/', {'asset_id': 1})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
