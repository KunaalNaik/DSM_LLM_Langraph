import streamlit as st

# Initialize the state
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to handle user input and generate response
def handle_input():
    user_input = st.text_input("You:", key="input")
    if user_input:
        st.session_state['messages'].append(("user", user_input))
        for event in graph.stream({"messages": st.session_state['messages']}):
            for value in event.values():
                st.session_state['messages'].append(("assistant", value["messages"]))
        st.experimental_rerun()

# Display the chat messages
st.title("Chatbot")
for role, message in st.session_state['messages']:
    if role == "user":
        st.text(f"You: {message}")
    else:
        st.text(f"Assistant: {message}")

# Input box for user to type their message
handle_input()