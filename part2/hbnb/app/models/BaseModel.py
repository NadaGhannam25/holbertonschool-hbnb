import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Update the updated_at timestamp."""
        self.updated_at = datetime.utcnow()

    def update(self, data: dict):
        """Update attributes from a dictionary, then refresh updated_at."""
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary.")

        for key, value in data.items():
            # protect core fields
            if key in ("id", "created_at", "updated_at"):
                continue
            if hasattr(self, key):
                setattr(self, key, value)

        self.save()
