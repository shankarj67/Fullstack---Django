from django.test import TestCase
from .models import ToDo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ToDo.objects.create(title='first todo')
        ToDo.objects.create(description='a description here')

    def test_title_content(self):
        todo = ToDo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')

    def test_description_content(self):
        todo = ToDo.objects.get(id=2)
        expected_object_name = f'{todo.description}'
        self.assertEquals(expected_object_name, 'a description here')