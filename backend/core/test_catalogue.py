from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.exceptions import ValidationError
from core.models import Category, Product

class CatalogueTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Produce', slug='produce')
        self.tomato = Product.objects.create(category=self.category, name='Tomatoes', unit='500 g pack', price_kobo=185000, stock=2, image_path='/images/sample-tomatoes.png')
        self.basket = Product.objects.create(category=self.category, name='Basket', unit='1 basket', price_kobo=500000, stock=0, is_basket=True)

    def test_public_catalogue_search_and_availability(self):
        response = self.client.get('/api/products/', {'search': 'tomato'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['products']), 1)
        self.assertTrue(response.json()['products'][0]['in_stock'])
        self.assertFalse(next(p for p in self.client.get('/api/products/').json()['products'] if p['name'] == 'Basket')['in_stock'])

    def test_basket_stock_is_independent(self):
        self.basket.stock = 3
        self.basket.save()
        self.tomato.refresh_from_db()
        self.assertEqual(self.tomato.stock, 2)

    def test_invalid_price_and_stock_rejected(self):
        self.tomato.price_kobo = -1
        self.tomato.stock = -1
        with self.assertRaises(ValidationError):
            self.tomato.full_clean()

    def test_writes_and_staff_management_require_authorisation(self):
        self.assertEqual(self.client.post('/api/products/', {}).status_code, 405)
        self.assertEqual(self.client.get('/staff/').status_code, 302)
        user = get_user_model().objects.create_user(username='customer', password='test-password')
        self.client.force_login(user)
        self.assertEqual(self.client.get('/staff/core/product/').status_code, 302)
    def test_category_filter_and_inactive_products(self):
        self.tomato.active = False
        self.tomato.save()
        response = self.client.get('/api/products/', {'category': 'produce'})
        self.assertEqual([p['name'] for p in response.json()['products']], ['Basket'])
        self.assertEqual(self.client.get('/api/products/', {'category': 'missing'}).json()['products'], [])

    def test_staff_with_product_permissions_can_change_stock(self):
        from django.contrib.auth.models import Permission
        staff = get_user_model().objects.create_user(username='stock-staff', password='test-password', is_staff=True)
        staff.user_permissions.add(*Permission.objects.filter(content_type__app_label='core', codename__in=['view_product', 'change_product']))
        self.client.force_login(staff)
        response = self.client.post(f'/staff/core/product/{self.tomato.pk}/change/', {'category': self.category.pk, 'name': self.tomato.name, 'unit': self.tomato.unit, 'price_kobo': self.tomato.price_kobo, 'stock': 9, 'active': 'on', 'image_path': self.tomato.image_path, '_save': 'Save'})
        self.assertEqual(response.status_code, 302)
        self.tomato.refresh_from_db()
        self.assertEqual(self.tomato.stock, 9)
        self.basket.refresh_from_db()
        self.assertEqual(self.basket.stock, 0)
    def test_staff_can_create_a_fixed_unit_product(self):
        from django.contrib.auth.models import Permission
        staff = get_user_model().objects.create_user(username='catalogue-staff', password='test-password', is_staff=True)
        staff.user_permissions.add(*Permission.objects.filter(content_type__app_label='core', codename__in=['view_product', 'add_product']))
        self.client.force_login(staff)
        response = self.client.post('/staff/core/product/add/', {'category': self.category.pk, 'name': 'New basket', 'unit': '1 basket', 'price_kobo': 700000, 'stock': 4, 'is_basket': 'on', 'active': 'on', '_save': 'Save'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.get(name='New basket').is_basket)
        self.assertEqual(self.tomato.stock, 2)

    def test_public_catalogue_exposes_availability_not_stock_counts(self):
        product = self.client.get('/api/products/').json()['products'][0]
        self.assertNotIn('stock', product)
    def test_product_detail_exposes_description_and_hides_inactive(self):
        self.tomato.description = 'A fixed sample pack.'
        self.tomato.save()
        response = self.client.get(f'/api/products/{self.tomato.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['description'], 'A fixed sample pack.')
        self.tomato.active = False
        self.tomato.save()
        self.assertEqual(self.client.get(f'/api/products/{self.tomato.pk}/').status_code, 404)

    def test_sorting_by_price_and_invalid_sort(self):
        response = self.client.get('/api/products/', {'sort': 'price-desc'})
        self.assertEqual([p['name'] for p in response.json()['products']], ['Basket', 'Tomatoes'])
        self.assertEqual(self.client.get('/api/products/', {'sort': 'invalid'}).status_code, 400)
    def test_staff_login_create_and_update_basket_through_management(self):
        staff = get_user_model().objects.create_superuser(username='review-staff', password='safe-test-password-123')
        login = self.client.post('/staff/login/?next=/staff/', {'username': staff.username, 'password': 'safe-test-password-123', 'next': '/staff/'})
        self.assertEqual(login.status_code, 302)
        create = self.client.post('/staff/core/product/add/', {'category': self.category.pk, 'name': 'Review basket', 'description': 'Example basket description', 'unit': '1 basket', 'price_kobo': 420000, 'stock': 3, 'is_basket': 'on', 'active': 'on', '_save': 'Save'})
        self.assertEqual(create.status_code, 302)
        basket = Product.objects.get(name='Review basket')
        update = self.client.post(f'/staff/core/product/{basket.pk}/change/', {'category': self.category.pk, 'name': basket.name, 'description': basket.description, 'unit': basket.unit, 'price_kobo': 430000, 'stock': 0, 'is_basket': 'on', 'active': 'on', '_save': 'Save'})
        self.assertEqual(update.status_code, 302)
        detail = self.client.get(f'/api/products/{basket.pk}/').json()
        self.assertEqual(detail['price_kobo'], 430000)
        self.assertFalse(detail['in_stock'])
        self.assertEqual(detail['description'], 'Example basket description')
        self.tomato.refresh_from_db()
        self.assertEqual(self.tomato.stock, 2)
