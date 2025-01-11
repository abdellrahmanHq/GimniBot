import streamlit as st  # Import Streamlit for creating the web app
import os  # Import os for environment variable management
import google.generativeai as genai  # Import Google's Generative AI SDK

st.title("Gemini Bot")  # Set the title of the Streamlit app

# Set the API key as an environment variable and configure the GenAI SDK
os.environ['GOOGLE_API_KEY'] = "AIzaSyCv48wNW2qoaF0egMiVNyrynfg9I5EHgwU"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Select and initialize the generative AI model
model = genai.GenerativeModel('gemini-pro')

# Initialize chat history if not already present in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",  # Role of the speaker
            "content": "Ask me Anything"  # Initial assistant message
        }
    ]

# Display chat history by iterating through session state messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):  # Create a chat bubble for the role
        st.markdown(message["content"])  # Display the content in Markdown format

# Function to process user queries and generate responses
def llm_function(query):
    response = model.generate_content(query)  # Send query to the AI model

    # Display the assistant's response
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # Append the user's query to the chat history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    # Append the assistant's response to the chat history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )

# Create an input box for the user to type their query
query = st.chat_input("What's up?")

# If the user submits a query, process and display it
if query:
    with st.chat_message("user"):  # Display the user's message
        st.markdown(query)

    llm_function(query)  # Call the function to handle the query and response
