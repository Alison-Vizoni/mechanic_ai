from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_KEY = os.getenv('API_KEY')
CHATBOT_MODEL_ID = os.getenv('CHATBOT_MODEL_ID')

POSTGRES_USER = os.getenv('POSTGRES_USER', 'chatbot')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'admin')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'postgres')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DB_NAME = os.getenv('POSTGRES_DB_NAME', 'langgraph_db')
DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}'
