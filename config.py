import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
    
    # Database
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME', 'rpo_bot')
    
    # Chat IDs
    GROUP_CHAT_ID = int(os.getenv('GROUP_CHAT_ID', '-1001234567890'))
    CHANNEL_CHAT_ID = int(os.getenv('CHANNEL_CHAT_ID', '-1001234567891'))
    
    # Content sources
    HABR_URL = "https://habr.com/ru/flows/develop/articles/"
    STACKOVERFLOW_URL = "https://api.stackexchange.com/2.3/questions"
