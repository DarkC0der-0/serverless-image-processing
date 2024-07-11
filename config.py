import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@db/image_processing')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
