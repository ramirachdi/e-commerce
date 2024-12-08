from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductTests(APITestCase):
    
    def setUp(self):
        """Create a sample product for testing."""
        self.product = Product.objects.create(
            name="Sample Product",
            description="A sample product for testing.",
            price=50.00,
            stock=10
        )
        self.valid_payload = {
            "name": "New Product",
            "description": "This is a new product.",
            "price": 100.00,
            "stock": 20
        }
        self.invalid_payload = {
            "name": "",
            "price": -10.00,
            "stock": -5
        }

    def test_create_product(self):
        """Test creating a new product (POST)."""
        response = self.client.post('/api/products/', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.valid_payload['name'])

    def test_get_products(self):
        """Test retrieving the list of products (GET)."""
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # Ensure at least one product exists
        self.assertEqual(response.data[0]['name'], self.product.name)

    def test_get_single_product(self):
        """Test retrieving a single product (GET /<id>/)."""
        response = self.client.get(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_update_product(self):
        """Test updating a product (PUT)."""
        update_payload = {
            "name": "Updated Product",
            "description": "Updated description.",
            "price": 75.00,
            "stock": 15
        }
        response = self.client.put(f'/api/products/{self.product.id}/', update_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_payload['name'])
        self.assertEqual(response.data['price'], update_payload['price'])

    def test_partial_update_product(self):
        """Test partial update of a product (PATCH)."""
        patch_payload = {"stock": 5}
        response = self.client.patch(f'/api/products/{self.product.id}/', patch_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['stock'], patch_payload['stock'])

    def test_delete_product(self):
        """Test deleting a product (DELETE)."""
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Ensure the product is deleted
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=self.product.id)

    def test_create_product_invalid(self):
        """Test creating a product with invalid data."""
        response = self.client.post('/api/products/', self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        self.assertIn('price', response.data)
