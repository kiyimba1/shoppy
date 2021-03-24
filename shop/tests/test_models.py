from django.test import TestCase

from shop.models import Category, Product


class CategoryTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test', slug='test')

    def setUp(self):
        pass

    def test_name_label(self):
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.name}'
        self.assertEqual(expected_object_name, str(category))

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_absolute_url(), '/en/test/')


class ProductTestClass(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        category = Category.objects.create(name='Test', slug='test')
        Product.objects.create(category=category, name='Test Product',
                               slug='test-product', description='Test description', price='100')

    def test_name(self):
        product = Product.objects.get(id=1)
        expected_name = f'{product.name}'
        self.assertEqual(expected_name, str(product))

    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.get_absolute_url(), '/en/1/test-product/')
