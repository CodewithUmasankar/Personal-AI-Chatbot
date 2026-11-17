from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-20b")

st.title("umasankar ChatBot")
st.markdown("My QnA Bot with LangChain and Groq!")

# Memory initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old chat history
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything ?")

if query:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    st.chat_message("user").markdown(query)

    # Send full history, not just current query
    res = llm.invoke(st.session_state.messages)

    # Show AI response
    st.chat_message("assistant").markdown(res.content)

    # Store AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": res.content
    })