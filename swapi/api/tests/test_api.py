import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from graphene.test import Client

from api.models import Planet,People,Film
from api.schema import schema

char_list_query="""
query{
  allPeople{
    id,
    name,
    films {
      edges {
        node {
          title
        }
      }
    }
  }
}
"""
char_sigle_query="""
query{
  fltName(name_Icontains: "luke") {
    edges {
      node {
        id,
        name
      }
    }
  }
}
"""
class TestApiSchema(TestCase):
  def setUp(self):
        self.client = Client(schema)
        self.people = mixer.blend(People)
        
  def test_char_sigle_query(self):
    response = self.client.execute(char_sigle_query, variable_values={"id": self.people.id})
    response_people = response.get("data").get("people")
    assert response_people["id"] == str(self.people.id)