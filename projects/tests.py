from django.contrib.auth.models import User
from .models import Project
from rest_framework import status
from rest_framework.test import APITestCase

class ProjectListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='admin', password='password')

    def test_can_list_projects(self):
        self.client.login(username='admin', password='password')
        admin = User.objects.get(username='admin')
        Project.objects.create(owner=admin, project_name='new project')
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_projects(self):
        self.client.login(username='admin', password='password')
        response = self.client.post('/projects/', {'project_name':'great project'})
        count = Project.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_list_projects(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print(response.data)
        print(len(response.data))

    def test_logged_out_user_cant_create_projects(self):
        response = self.client.post('/projects/', {'project_name':'title of peppe'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProjectDetailViewTests(APITestCase):
    def setUp(self):
        admin = User.objects.create_user(username='admin', password='pass')
        fabio = User.objects.create_user(username='fabio', password='pass')
        Project.objects.create(
            owner=admin,
            project_name='a title',
            content='admins content'
        )
        Project.objects.create(
            owner=fabio,
            project_name='another title',
            content='fabios content'
        )

    def test_can_retrieve_project_using_valid_id(self):
        self.client.login(username='admin', password='pass')
        response = self.client.get('/projects/1/')
        self.assertEqual(response.data['project_name'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_project_using_valid_id(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_fetch_project_by_invalid_id(self):
        self.client.login(username='admin', password='pass')
        response = self.client.get('/projects/a/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_project(self):
        self.client.login(username='admin', password='pass')
        response = self.client.put('/projects/1/', {'project_name':'new title'})
        project = Project.objects.filter(pk=1).first()
        self.assertEqual(project.project_name, 'new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_project_dont_own(self):
        self.client.login(username='admin', password='pass')
        response = self.client.put('/projects/2/', {'project_name':'new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)