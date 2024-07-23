import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = "**************************" #google ai key

# Initialize the language model
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)