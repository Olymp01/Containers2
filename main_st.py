import pandas as pd
import streamlit as st
from io import BytesIO
from datetime import datetime
import psycopg2

def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from autorization;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")




        


