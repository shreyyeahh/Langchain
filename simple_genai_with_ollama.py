import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os 
from dotenv import load_dotenv
load_dotenv()

# Load environment variables from .env file
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates English to French."),
        ("user","Question:{question}")
    ]
)

#Streamlit framework 
st.title("langchain demo with LLAMA3")
input_text = st.text_input("What question do you have?")

##Ollama llama3 model calling
llm = Ollama(model = "llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text})) # this will call the LLM and display the output
    # we are passing the input_text to the chain which will process it through the prompt, LLM, and output parser
