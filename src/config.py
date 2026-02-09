"""Configuration du projet GameTracker ETL."""

import os

class Config:
    """Configuration centralisée via variables d'environnement."""

    DB_HOST = os.environ.get('DB_HOST', 'db')
    DB_PORT = int(os.environ.get('DB_PORT', 3306))
    DB_NAME = os.environ.get('DB_NAME', 'gametracker_db')
    DB_USER = os.environ.get('DB_USER', 'user_tracker')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password_tracker')
    DATA_DIR = os.environ.get('DATA_DIR', '/app/data')
    OUTPUT_DIR = os.environ.get('OUTPUT_DIR', '/app/output')
