import datetime

import factory
import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserList:
    def test_empty_list(self, client):
        """
        User successfully gets user's list page while non user exists
        """
        url = reverse('users:list')
        response = client.get(url)
        assert response.status_code == 200
        assert 'There is no users yet' in str(response.content)

    def test_list(self, client, users):
        """
        User successfully gets user's list page
        """
        url = reverse('users:list')
        response = client.get(url)
        assert response.status_code == 200
        for user in users:
            assert user.username in str(response.content)


class TestUserDetail:
    def test_detail(self, client, users):
        """
        User successfully gets user's detail page
        """
        user = users[0]
        url = reverse('users:detail', args=(user.pk,))
        response = client.get(url)
        assert response.status_code == 200
        assert user.username in str(response.content)

    def test_detail_user_does_not_exists(self, client, users):
        """
        User gets detail page of not existing user and get 404 error
        """
        user = users[0]
        url = reverse('users:detail', args=(user.pk + 100,))
        response = client.get(url)
        assert response.status_code == 404


class TestUserUpdate:
    def test_update(self, client, users):
        """
        User successfully update user's data
        """
        user = users[0]
        data = factory.build(dict, FACTORY_CLASS=UserFactory)
        url = reverse('users:update', args=(user.pk,))
        response = client.post(url, data)
        assert response.status_code == 302
        assert response.url == reverse('users:list')

        user.refresh_from_db()
        assert user.username == data['username']
        assert user.birthday == datetime.datetime.strptime(data['birthday'], '%Y-%m-%d').date()

    def test_empty_data(self, client, users):
        """
        User submits empty form and gets error messages
        """
        user = users[0]
        url = reverse('users:update', args=(user.pk,))
        response = client.post(url)
        assert response.status_code == 200
        assert 'This field is required.' in str(response.content)

    def test_invalid_data(self, client, users):
        """
        User submits invalid data and gets error messages
        """
        user = users[0]
        data = {
            'username': '*' * 255,
            'birthday': 'test'
        }
        url = reverse('users:update', args=(user.pk,))
        response = client.post(url, data)
        assert response.status_code == 200
        assert 'Enter a valid date.' in str(response.content)
        assert 'Ensure this value has at most 150 characters (it has 255).' in str(response.content)

    def test_username_not_unique(self, client, users):
        """
        User submits username which already exists and gets error message
        """
        user = users[0]
        data = factory.build(dict, FACTORY_CLASS=UserFactory, username=users[1].username)
        url = reverse('users:update', args=(user.pk,))
        response = client.post(url, data)
        assert response.status_code == 200
        assert 'A user with that username already exists.' in str(response.content)


class TestUserDelete:

    def test_delete(self, client, users):
        """
        User successfully delete another user
        """
        user = users[0]
        url = reverse('users:delete', args=(user.pk,))
        response = client.get(url)
        assert response.status_code == 405
        response = client.post(url)
        assert response.status_code == 302
        assert response.url == reverse('users:list')
        assert not get_user_model().objects.filter(pk=user.pk).exists()

    def test_delete_user_does_not_exists(self, client, users):
        """
        User deletes not existing user and gets 404 error
        """
        user = users[0]
        url = reverse('users:delete', args=(user.pk + 100,))
        response = client.post(url)
        assert response.status_code == 404


class TestUserCreate:

    def test_create(self, client):
        """
        User successfully create new user
        """
        count = get_user_model().objects.count()
        data = factory.build(dict, FACTORY_CLASS=UserFactory)
        url = reverse('users:create')
        response = client.post(url, data)
        assert response.status_code == 302

        user = get_user_model().objects.last()
        assert user.username == data['username']
        assert user.birthday == datetime.datetime.strptime(data['birthday'], '%Y-%m-%d').date()
        assert get_user_model().objects.count() == count + 1

    def test_empty_data(self, client):
        """
        User submits empty form and gets error messages
        """
        url = reverse('users:create')
        response = client.post(url)
        assert response.status_code == 200
        assert 'This field is required.' in str(response.content)

    def test_invalid_data(self, client):
        """
        User submits invalid data and gets error messages
        """
        data = {
            'username': '*' * 255,
            'birthday': 'test'
        }
        url = reverse('users:create')
        response = client.post(url, data)
        assert response.status_code == 200
        assert 'Enter a valid date.' in str(response.content)
        assert 'Ensure this value has at most 150 characters (it has 255).' in str(response.content)

    def test_username_not_unique(self, client, users):
        """
        User submits username which already exists and gets error message
        """
        data = factory.build(dict, FACTORY_CLASS=UserFactory, username=users[1].username)
        url = reverse('users:create')
        response = client.post(url, data)
        assert response.status_code == 200
        assert 'A user with that username already exists.' in str(response.content)
