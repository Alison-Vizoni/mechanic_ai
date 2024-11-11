from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
CHATBOT_MODEL_ID = os.getenv('CHATBOT_MODEL_ID')

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
