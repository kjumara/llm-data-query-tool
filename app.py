"""
Application Script to:
1. Accept natural language questions from the user
2. Send questions to an LLM with the dataset schema for conversion to Pandas Query
3. Parse and execute the generated query on the DataFrame
4. Return results as both summary text and DataFrame subsets

Intended as main entry point for the LLM-Powered Data Query Tool project
"""
from fontTools.misc.cython import returns

from load_data import load_data # File to Load Data
from config import api_key # loads from .env via config
from plot_utils import auto_chart # returns matplotlib chart

import pandas as pd
from openai import OpenAI
import streamlit as st

# Application Title
st.title("AI-Powered Data Q&A")

# load dataset using load_data.py
df = load_data("sales_data_sample.csv")
st.write("Using Default Sample Dataset")
st.write(df.head())


# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Implement user query
st.markdown(
    """
    💡 **Try asking questions like:**
    - What were total sales by year?
    - Show me sales by product line.
    - What were the top 5 bestselling product lines in 2003?
    """
)
user_question = st.text_input("Ask a question about the dataset: ")

# Create placeholders to update after question
answer_placeholder = st.empty()
chart_placeholder = st.empty()
table_placeholder = st.empty()

# Function to send question to LLM and get a Pandas query string
def question_to_query(user_question, df_schema):
    prompt = f"""
    Convert the following natural language question into a single valid Pandas expression 
    that can be executed directly on the DataFrame `df`.
    
    Rules:
    - Do not include imports, explanations, or code fences
    - Do not define variables (no `total_sales_per_year = ...`)
    - Output only one expression (ex. df.groupby('YEAR_ID')['SALES'].sum().reset_index())
    
    DataFrame Schema:
    {df_schema}
    
    User Question:
    {user_question}
    """
    # noinspection PyTypeChecker
    response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user",
                                                                              "content": prompt}], max_tokens=200)
    return response.choices[0].message.content.strip()

if user_question:
    # Build schema string to feed into LLM
    df_schema = df.dtypes.astype(str).to_dict()
    try:
        # Run LLM-generated query in Pandas
        query_str = question_to_query(user_question, df_schema)
    except Exception as e:
        st.error(f"Failed to generate a query: {e}")
try:
    df_prompted = pd.DataFrame()
    df_prompted = eval(query_str, {"df": df, "pd": pd})
except Exception as e:
    st.warning(f"Could not execute the generated query: {e}")

if df_prompted.empty:
    st.info("Query returned no results. Try rephrasing your question.")
else:
    # Show AI generated answer text
    answer_placeholder.write(f"**Answer:** I ran the query:\n{query_str}\n)")

    #create chart
    fig = auto_chart(df_prompted)
    if fig:
        chart_placeholder.pyplot(fig)

    #show table
    table_placeholder.dataframe(df_prompted)