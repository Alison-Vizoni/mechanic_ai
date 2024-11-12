from typing import Literal
from uuid import uuid4

from langchain.chains.conversation.base import ConversationChain
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langgraph.constants import START, END
from langgraph.graph import StateGraph, MessagesState

from chatbot.db import MemoryDB
from chatbot.prompts.prompt import get_prompt
from config import settings


class Chatbot:
    def __init__(self):
        self.chatbot_model_id = settings.CHATBOT_MODEL_ID
        self.model = ChatGroq(api_key=settings.API_KEY, model_name=self.chatbot_model_id, temperature=0)
        self.state_graph = StateGraph(state_schema=MessagesState)
        self.memory = MemoryDB('session_1')
        self.system_prompt = get_prompt()

        self.conversation_chain = ConversationChain()

    def ask_question(self, question):
        app = self._get_app()

        system_message = self._get_system_message()
        input_message = HumanMessage(content=question)
        config = {"configurable": {"thread_id": uuid4()}}

        final_state = app.invoke(input=[system_message, input_message], config=config)

        response_message = final_state.get('messages', [None])[-1]
        if response_message and hasattr(response_message, 'content'):
            return response_message.content
        return 'Houve alguma falha durante o processamento. Tente novamente.'

    def call_model(self, state: MessagesState):
        messages = state['messages']
        response = self.model.invoke(messages)

        return {'messages': [response]}

    def should_continue(self, state: MessagesState) -> Literal["tools", END]:
        messages = state.get('messages', [None])
        last_message = messages[-1]
        if last_message and last_message.tool_calls:
            return 'tools'
        return END

    def _get_app(self):
        self.state_graph.add_node('agent', self.call_model)
        self.state_graph.add_edge(START, 'agent')
        self.state_graph.add_conditional_edges('agent', self.should_continue)
        return self.state_graph.compile(checkpointer=self.memory)

    def _get_system_message(self):
        content = [
            f'Template: {self.system_prompt}',
        ]
        return SystemMessage(content=content)
