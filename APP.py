import streamlit as st
from mistralai import Mistral, UserMessage
import os

# Load API Key
api_key = "write your api here"

def mistral_response(user_message):
    client = Mistral(api_key=api_key)
    messages = [UserMessage(content=user_message)]
    chat_response = client.chat.complete(model="mistral-large-latest", messages=messages)
    return chat_response.choices[0].message.content

# Streamlit UI
st.title("Bank Customer Support Chatbot")
user_input = st.text_input("Ask me a question:")

if st.button("Submit"):
    response = mistral_response(user_input)
    st.write("### Response:", response)
