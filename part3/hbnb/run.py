import os
from app import create_app
from config import DevelopmentConfig, ProductionConfig
from app.extensions import db

def get_config():
    env = os.getenv("FLASK_ENV", "development").lower()
    if env == "production":
        return ProductionConfig
    return DevelopmentConfig

# Create Flask app
app = create_app(get_config())

# Initialize database tables
with app.app_context():
    from app.models.user import User  
    from app.models.place import Place  
    from app.models.review import Review 
    from app.models.amenity import Amenity 
    db.create_all()

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",  # Use 127.0.0.1 for development
        port=5000,
        debug=True
    )
