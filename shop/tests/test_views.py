from django.http import response
from django.test import TestCase
from django.urls import reverse

from shop.models import Category, Product


class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        category = Category.objects.create(name='Test', slug='test')
        Product.objects.create(category=category, name='Test Product',
                               slug='test-product', description='Test  dscription', price='100')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/en/')
        self.assertEqual(response.status_code, 200)

    def test_view_by_category(self):
        response = self.client.get('/en/test/')
        self.assertEqual(response.status_code, 200)

    def test_error_code_unavailable_category(self):
        response = self.client.get('/en/unknown/')
        self.assertEqual(response.status_code, 404)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/list.html')


class ProductDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        category = Category.objects.create(name='Test', slug='test')
        product = Product.objects.create(category=category, name='Test Product',
                                         slug='test-product', description='Test  dscription', price='100')

    # def test_view_url_product(self):

    #     response = self.client.get(reverse('shop:product_detail', kwargs={
    #                                'id': '1', 'slug': 'test-product'}))
    #     self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('shop:product_detail', kwargs={
                                   'id': '1', 'slug': 'test-product'}))
        self.assertTemplateUsed(response, 'shop/product/detail.html')
