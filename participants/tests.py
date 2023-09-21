from django.contrib.auth.models import User
from .models import Participant, Project
from rest_framework import status
from rest_framework.test import APITestCase


class ParticipantListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='admin', password='password')
        

    def test_can_list_participants(self):
        self.client.login(username='admin', password='password')
        response = self.client.get('/participants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data) here for debugging
        # print(len(response.data)) here for debugging

    def test_logged_in_user_can_participate_to_a_project(self):
        self.client.login(username='admin', password='password')
        admin = User.objects.get(username='admin')
        Project.objects.create(owner=admin, project_name='new project')
        response = self.client.post('/participants/', {'project_id':1})
        count = Participant.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_in_user_cant_participate_to_a_project_twotimes(self):
        self.client.login(username='admin', password='password')
        admin = User.objects.get(username='admin')
        Project.objects.create(owner=admin, project_name='new project')
        self.client.post('/participants/', {'project_id':1})
        response = self.client.post('/participants/', {'project_id':1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logged_out_user_cant_retrieve_list_of_participants(self):
        response = self.client.get('/participants/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)        


class ParticipantDetailViewTests(APITestCase):
    def setUp(self):
        admin = User.objects.create_user(username='admin', password='pass')
        fabio = User.objects.create_user(username='fabio', password='pass')
        Project.objects.create(
            owner=admin,
            project_name='a title',
            content='admins content'
        )
        self.client.login(username='fabio', password='pass')
        self.client.post('/participants/', {'project_id':1})
    
    def test_logged_in_user_and_owner_can_delete_participation(self):
        self.client.login(username='admin', password='pass')
        self.client.post('/participants/', {'project_id':2})
        self.client.delete('/participants/2/')
        response = self.client.get('/participants/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_and_not_owner_cant_delete_participation(self):
        self.client.login(username='admin', password='pass')
        response = self.client.delete('/participants/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_retrieve_detail_of_participation(self):
        response = self.client.get('/participants/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)