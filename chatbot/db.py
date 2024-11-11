from langchain.memory.chat_message_histories import RedisChatMessageHistory

from config import settings


class MemoryDB:
    def __init__(self, session_id):
        url = f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0'
        self.redis_client = RedisChatMessageHistory(url=url, session_id=session_id)
