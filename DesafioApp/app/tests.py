from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient, APITestCase, APIRequestFactory

# Create your tests here.

class TaskFactoryTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_login_required(self):
        request = self.factory.get('/')
        request.user = User.objects.create_user(username='test', password='test1234')

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {'title': 'Test Task', 'description': 'Test Description', 'due_date': '2020-02-20'}, auth=('test', 'test1234'))
        return Response(response, status=status.HTTP_201_CREATED)

    def test_update_task(self):
        response = self.client.put('/api/tasks/1/', {'title' : 'Modify Task'})
        return Response(response, status=status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete('/api/tasks/1/')
        return Response(response, status=status.HTTP_204_NO_CONTENT)

    def test_list_tasks(self):
        response = self.client.get('/api/tasks/')
        return Response(response, status=status.HTTP_200_OK)

class TaskTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='testuser', password='ab121314')
        self.client = APIClient()

    def login(self):
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'ab121314'}, format='json')
        return response.data['access']

    def test_create(self):
        token = self.login()

        response = self.client.post(
            '/api/tasks/',
            {
                "title": "Tarefa 3",
                "description": "Executar Tarefa 3",
                "due_date": "2024-08-02"
            },
            format='json',
            headers={'Authorization': 'Bearer ' + token}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        token = self.login()
        response = self.client.get('/api/tasks/', format='json', headers={'Authorization': 'Bearer ' + token})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

