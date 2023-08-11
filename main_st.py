import pandas as pd
import streamlit as st
from io import BytesIO
from datetime import datetime
import psycopg2


conn = psycopg2.connect(dbname='postgres', user='postgres', 
                        password='1', host='localhost')
cursor = conn.cursor()
cursor.execute('SELECT * FROM autorization')
records = cursor.fetchall()
st.write(records)
cursor.close()
conn.close()




        


