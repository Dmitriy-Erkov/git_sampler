import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    CSRF_ENABLE = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.getenv('SECRET_KEY_default')
