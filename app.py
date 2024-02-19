import pandas as pd
import streamlit as st
from utils import query_agent
from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv
load_dotenv()


def query_agent(data, query):
    df = pd.read_csv(data)
    llm = OpenAI()
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    return agent.run(query)

st.title("Let's do some analysis on your csv📝")
st.header("Please upload your csv file here⬇️:")
          
data = st.file_uploader("Upload csv file", type="csv")
query = st.text_area("Enter your query")
button = st.button("Generate Response")

if button:
    answer = query_agent(data=data, query=query)
    st.write(answer)