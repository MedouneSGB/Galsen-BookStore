import os


class Config:
    SECRET_KEY = "loveDjango"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_MODIFICATIONS = False
    DEBUG = True
    UPLOAD_FOLDER = 'uploads/images'
    UPLOADED_PHOTOS_DEST = os.getcwd()
    STATIC_FOLDER = 'static'
