import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.validation import Validator, ValidationError
from app.models.user import User
from app.models.place import Place
from app.models.review import Review

class TestValidation(unittest.TestCase):
    """Test validation logic"""
    
    def test_email_validation(self):
        """Test email validation"""
        self.assertEqual(Validator.validate_email("test@example.com"), "test@example.com")
        
        with self.assertRaises(ValidationError):
            Validator.validate_email("invalid-email")
        
        with self.assertRaises(ValidationError):
            Validator.validate_email("")
    
    def test_password_validation(self):
        """Test password validation"""
        self.assertEqual(Validator.validate_password("password123"), "password123")
        
        with self.assertRaises(ValidationError):
            Validator.validate_password("short")
        
        with self.assertRaises(ValidationError):
            Validator.validate_password("")
    
    def test_string_validation(self):
        """Test string validation"""
        self.assertEqual(Validator.validate_string("Hello", "Test"), "Hello")
        
        with self.assertRaises(ValidationError):
            Validator.validate_string("", "Test")
        
        with self.assertRaises(ValidationError):
            Validator.validate_string(123, "Test")
    
    def test_uuid_validation(self):
        """Test UUID validation"""
        valid_uuid = "123e4567-e89b-12d3-a456-426614174000"
        self.assertEqual(Validator.validate_uuid(valid_uuid, "ID"), valid_uuid)
        
        with self.assertRaises(ValidationError):
            Validator.validate_uuid("invalid", "ID")
    
    def test_rating_validation(self):
        """Test rating validation"""
        self.assertEqual(Validator.validate_rating(3), 3)
        self.assertEqual(Validator.validate_rating(0), 0)
        self.assertEqual(Validator.validate_rating(5), 5)
        
        with self.assertRaises(ValidationError):
            Validator.validate_rating(6)
        
        with self.assertRaises(ValidationError):
            Validator.validate_rating(-1)
    
    def test_user_model_validation(self):
        """Test User model validation"""
        # Valid user
        user = User("test@example.com", "password123", "John", "Doe")
        self.assertEqual(user.email, "test@example.com")
        
        # Invalid email
        with self.assertRaises(ValidationError):
            User("invalid", "password123")
    
    def test_place_model_validation(self):
        """Test Place model validation"""
        # Valid place
        place = Place("Beautiful Villa", "123e4567-e89b-12d3-a456-426614174000", "Luxury villa", 500)
        self.assertEqual(place.title, "Beautiful Villa")
        
        # Invalid price
        with self.assertRaises(ValidationError):
            Place("Test", "123e4567-e89b-12d3-a456-426614174000", "Test", -100)

if __name__ == '__main__':
    unittest.main()
