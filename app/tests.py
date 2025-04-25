from django.test import TestCase
import pytest
from rest_framework.test import APIClient
# Create your tests here.


@pytest.mark.django_db
def test_getPersonagens():
    client = APIClient()
    response = client.get('/api/personagens/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
