import unittest
import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.services.facade import facade

class TestAPI(unittest.TestCase):
    """Test cases for HBnB API"""
    
    def setUp(self):
        """Set up test client"""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # Clear data before each test
        facade.user_repo._data.clear()
        facade.place_repo._data.clear()
        facade.review_repo._data.clear()
    
    def test_create_user_success(self):
        """Test successful user creation"""
        response = self.client.post('/api/v1/users/', 
                                   json={
                                       "email": "test@example.com",
                                       "password": "password123",
                                       "first_name": "John",
                                       "last_name": "Doe"
                                   })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("id", data)
        self.assertEqual(data["email"], "test@example.com")
    
    def test_create_user_missing_email(self):
        """Test user creation with missing email"""
        response = self.client.post('/api/v1/users/', 
                                   json={
                                       "password": "password123"
                                   })
        self.assertEqual(response.status_code, 400)
    
    def test_create_user_invalid_email(self):
        """Test user creation with invalid email"""
        response = self.client.post('/api/v1/users/', 
                                   json={
                                       "email": "invalid-email",
                                       "password": "password123"
                                   })
        self.assertEqual(response.status_code, 400)
    
    def test_create_place_success(self):
        """Test successful place creation"""
        # First create a user
        user_resp = self.client.post('/api/v1/users/', 
                                    json={
                                        "email": "owner@test.com",
                                        "password": "pass123"
                                    })
        user_data = json.loads(user_resp.data)
        user_id = user_data["id"]
        
        # Then create a place
        response = self.client.post('/api/v1/places/', 
                                   json={
                                       "title": "Beautiful Apartment",
                                       "owner_id": user_id,
                                       "description": "Luxury apartment",
                                       "price_per_night": 150
                                   })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("id", data)
        self.assertEqual(data["title"], "Beautiful Apartment")
    
    def test_create_place_invalid_owner(self):
        """Test place creation with invalid owner ID"""
        response = self.client.post('/api/v1/places/', 
                                   json={
                                       "title": "Test Place",
                                       "owner_id": "invalid-uuid-format",
                                       "price_per_night": 100
                                   })
        self.assertEqual(response.status_code, 400)
    
    def test_get_all_users(self):
        """Test retrieving all users"""
        # Create some users
        self.client.post('/api/v1/users/', json={"email": "user1@test.com", "password": "pass1"})
        self.client.post('/api/v1/users/', json={"email": "user2@test.com", "password": "pass2"})
        
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
    
    def test_review_validation(self):
        """Test review validation"""
        # Create user and place first
        user_resp = self.client.post('/api/v1/users/', json={"email": "reviewer@test.com", "password": "pass"})
        user_data = json.loads(user_resp.data)
        
        place_resp = self.client.post('/api/v1/places/', 
                                     json={
                                         "title": "Review Place",
                                         "owner_id": user_data["id"],
                                         "price_per_night": 100
                                     })
        place_data = json.loads(place_resp.data)
        
        # Test invalid rating
        response = self.client.post('/api/v1/reviews/', 
                                   json={
                                       "text": "Good place",
                                       "user_id": user_data["id"],
                                       "place_id": place_data["id"],
                                       "rating": 10  # Invalid, should be 0-5
                                   })
        self.assertEqual(response.status_code, 400)
    
    def test_swagger_documentation(self):
        """Test Swagger documentation endpoint"""
        response = self.client.get('/swagger.json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("swagger", data)
        self.assertIn("paths", data)

if __name__ == '__main__':
    unittest.main()
