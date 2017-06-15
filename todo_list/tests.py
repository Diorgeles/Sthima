# coding=utf-8
from django.test import TestCase, Client

from django.core.urlresolvers import reverse

from model_mommy import mommy

from todo_list.models.item_list import Item_list

class ViewTestCase(TestCase):
    """Alguns testes basicos"""
    def setUp(self):
        self.url = reverse('todolist:todo_list')
        self.client = Client()
        self.itens = mommy.make('Item_list', _quantity=10)

    def tearDown(self):
        Item_list.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('itens_list' in response.context)
        product_list = response.context['itens_list']
        self.assertEquals(product_list.count(), 10)
