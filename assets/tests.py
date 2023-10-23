from django.contrib.auth.models import User
from .models import Asset
from .models import Project
from rest_framework import status
from rest_framework.test import APITestCase


class AssetListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='admin', password='password')

    def test_can_list_assets(self):
        self.client.login(username='admin', password='password')
        admin = User.objects.get(username='admin')
        project = Project.objects.create(
            owner=admin, project_name='new project')
        Asset.objects.create(
            owner=admin,
            asset_name='new asset',
            project_id=project
            )
        response = self.client.get('/assets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_assets(self):
        response = self.client.post('/assets/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


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
            owner=admin,
            asset_name='new asset',
            project_id=project
            )

    def test_logged_in_user_can_see_asset_detail(self):
        self.client.login(username='fabio', password='pass')
        response = self.client.get('/assets/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_and_Asset_owner_can_delete_asset(self):
        self.client.login(username='admin', password='pass')
        # self.client.post('/assets/',{'asset_name':'Peppe'})
        self.client.delete('/assets/1/')
        response = self.client.get('/assets/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_and_Asset_owner_can_delete_asset(self):
        self.client.login(username='fabio', password='pass')
        # self.client.post('/assets/',{'asset_name':'Peppe'})
        response = self.client.delete('/assets/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
