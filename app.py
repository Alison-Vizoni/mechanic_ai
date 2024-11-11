import streamlit
from chatbot.chatbot import Chatbot

chatbot = Chatbot()

streamlit.title("Chatbot de Mecânica")

user_input = streamlit.text_input("Digite sua pergunta sobre mecânica:")

if user_input:
    response = chatbot.ask_question(user_input)
    streamlit.write(f"Resposta: {response}")
