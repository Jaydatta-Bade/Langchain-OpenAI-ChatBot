import streamlit as st
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import time
import logging

# Configure logging
logging.basicConfig(
    filename="chatbot.log",  # Log file name
    level=logging.INFO,      # Log level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
)

# Streamlit Sidebar for OpenAI API Key
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# Validate API Key
if not api_key:
    st.sidebar.warning("Please enter your OpenAI API key to continue.")
    logging.warning("No API key provided. Application stopped.")
    st.stop()

logging.info("API key provided. Initializing ChatOpenAI model.")

# Initialize the ChatOpenAI model with the provided API key
llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo", openai_api_key=api_key)

# Initialize memory for the conversation
memory = ConversationBufferMemory()

# Create a conversation chain
conversation = ConversationChain(llm=llm, memory=memory)

# Streamlit UI
st.title("Langchain OpenAI Chatbot")
st.write("This is a basic conversational chatbot powered by OpenAI, LangChain, and Streamlit.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]
    logging.info("Chat history initialized.")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if user_input := st.chat_input("Type your message here..."):
    logging.info(f"User input received: {user_input}")

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get the response from the conversation chain
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            response = conversation.run(input=user_input)
            logging.info(f"Assistant response generated: {response}")
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            response = "Sorry, I encountered an error while processing your request."

        # Simulate stream of response with milliseconds delay
        for chunk in response.split():
            full_response += chunk + " "
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.05)
        message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    logging.info("Response added to chat history.")