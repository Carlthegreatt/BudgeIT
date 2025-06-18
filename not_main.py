from transformers import pipeline
import sqlite3
import pandas as pd
import tabulate


def load_table(db_path, table_name):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df


def ask_with_huggingface(prompt: str):
    summarizer = pipeline("text-generation", model="google/flan-t5-base")
    return summarizer(prompt, max_length=256)[0]["generated_text"]


def build_prompt(df: pd.DataFrame, question: str):
    sample = df.head(10).to_markdown()  # only show a few rows
    prompt = f"""You are a data analyst AI.
Here is a sample of the table:

{sample}

Question: {question}
Give your analysis and suggestion.
"""
    return prompt


df = load_table("accounts.db", "transactions")
prompt = build_prompt(df, "What insights can you provide from this data?")
reply = ask_with_huggingface(prompt)

print("AI Suggestion:")
print(reply)
