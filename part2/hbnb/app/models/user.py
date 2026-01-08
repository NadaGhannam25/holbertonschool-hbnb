from app.models.BaseModel import BaseModel

class User(BaseModel):
    def __init__(self, email, password, first_name="", last_name=""):
        super().__init__()
        
        # Basic validation
        if not email or '@' not in email:
            raise ValueError("Invalid email format")
        
        if not password or len(password) < 6:
            raise ValueError("Password must be at least 6 characters")
        
        self.email = email
        self.password = password
        self.first_name = first_name or ""
        self.last_name = last_name or ""
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        })
        return data
