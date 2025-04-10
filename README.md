# Langchain-OpenAI-ChatBot

This is a conversational chatbot built using **LangChain**, **OpenAI's GPT-3.5-turbo**, and **Streamlit**. The chatbot maintains context across conversations using LangChain's memory capabilities and provides a user-friendly interface powered by Streamlit.

## Features

- **OpenAI GPT-3.5-turbo Integration**: Uses OpenAI's powerful language model for generating responses.
- **LangChain Memory**: Maintains conversation context for a seamless chat experience.
- **Streamlit Frontend**: Provides an interactive and easy-to-use chat interface.
- **API Key Input**: Securely input your OpenAI API key through the Streamlit sidebar.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or later
- Pip (Python package manager)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Jaydatta-Bade/Langchain-OpenAI-ChatBot.git
   cd Langchain-OpenAI-ChatBot
   ```
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    If requirements.txt is not available, install the dependencies manually:
    ```
    pip install openai langchain streamlit streamlit-chat tiktoken python-dotenv langchain-community
    ```

## Usage

1. Run the Streamlit app:
    ```
    streamlit run app.py
    ```
2. Open the URL provided by Streamlit in your browser (e.g., http://localhost:8501).

3. Enter your OpenAI API key in the Settings sidebar to authenticate.

4. Start chatting with the bot by typing your messages in the input box.


## Notes
- Ensure you have a valid OpenAI API key to use this application.
- The chatbot uses a simulated typing effect for responses to enhance the user experience.
