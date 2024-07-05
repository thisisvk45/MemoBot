import streamlit as st
from utils import *

st.title("Chatbot (with memory)")
st.header("Let's chat!")

if "context" not in st.session_state:
    st.session_state["context"] = ""
if "history" not in st.session_state:
    st.session_state["history"] = []

def display_chat_history():
    for chat in st.session_state["history"]:
        st.write(f"**User:** {chat['user']}")
        st.write(f"**Bot:** {chat['bot']}")

user_query = st.text_input("Enter your message.")
submit = st.button("Respond")

reset = st.button("Reset current session")
if reset:
    st.session_state["context"] = ""
    st.session_state["history"] = []

if submit:
    if user_query:
        context = st.session_state["context"]

        con_query = contextualize(user_query, context)
        query_response = generate_response(con_query)
        new_context = generate_context(context, con_query, query_response)

        # Store new context and history in session
        st.session_state["context"] = new_context
        st.session_state["history"].append({"user": user_query, "bot": query_response})

        # Display chat history
        st.success(query_response)

    else:
        st.error("Please enter a query!!!")

# Display previous chat history
display_chat_history()
