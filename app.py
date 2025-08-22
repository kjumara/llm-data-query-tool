"""
Application Script to:
1. Accept natural language questions from the user
2. Send questions to an LLM with the dataset schema for conversion to Pandas Query
3. Parse and execute the generated query on the DataFrame
4. Return results as both summary text and DataFrame subsets

Intended as main entry point for the LLM-Powered Data Query Tool project
"""

from load_data import load_data, summarize_data
from config import api_key
from openai import OpenAI
import pandas as pd

# load dataset using load_data.py
df = load_data("sales_data_sample.csv")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Implement user query
user_question = input("Enter your question about the dataset: ")

# Build schema string to feed into LLM
df_schema = str(df.dtypes)

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

# Run LLM-generated query in Pandas
query_str = question_to_query(user_question, df_schema)
print(query_str)
df_prompted = pd.DataFrame()
try:
    df_prompted = eval(query_str, {"df": df, "pd": pd})
except Exception as e:
    print(f"Error executing query: {e}")

# Show results
print("\n--- Query Results ---")
print(df_prompted.head())
print("\n--- Summary Results ---")
summary = summarize_data(df_prompted)