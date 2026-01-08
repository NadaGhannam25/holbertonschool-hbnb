"""
Simple validation module for Task 6
"""

class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

class Validator:
    """Basic validation utilities"""
    
    @staticmethod
    def validate_email(email):
        """Simple email validation"""
        if not email:
            raise ValidationError("Email is required")
        
        if '@' not in email or '.' not in email:
            raise ValidationError("Invalid email format")
        
        return email
    
    @staticmethod
    def validate_password(password):
        """Simple password validation"""
        if not password:
            raise ValidationError("Password is required")
        
        if len(password) < 6:
            raise ValidationError("Password must be at least 6 characters")
        
        return password
    
    @staticmethod
    def validate_string(value, field_name, required=True):
        """Simple string validation"""
        if required and (not value or value.strip() == ""):
            raise ValidationError(f"{field_name} is required")
        
        return str(value) if value else ""
