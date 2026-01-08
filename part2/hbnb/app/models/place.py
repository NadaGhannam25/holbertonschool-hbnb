from app.models.BaseModel import BaseModel
from app.models.validation import Validator, ValidationError

class Place(BaseModel):
    def __init__(self, title, owner_id, description="", price_per_night=0):
        super().__init__()
        
        # Validate inputs
        self.title = Validator.validate_string(title, "Title", min_length=1, max_length=100)
        self.owner_id = Validator.validate_uuid(owner_id, "Owner ID")
        self.description = Validator.validate_string(description, "Description", min_length=0, max_length=500)
        self.price_per_night = Validator.validate_number(price_per_night, "Price per night", min_value=0)
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "title": self.title,
            "owner_id": self.owner_id,
            "description": self.description,
            "price_per_night": self.price_per_night
        })
        return data
