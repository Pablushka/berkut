from dotenv_config import Config
from cryptography.fernet import Fernet


settings = Config('.env')
SECRET_KEY = Fernet(settings('SECRET_KEY'))
