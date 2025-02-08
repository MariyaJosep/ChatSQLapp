from dotenv import load_dotenv
load_dotenv()  # Load all environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to Load Google Gemini Model and generate SQL query
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query results from SQLite database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows if rows else ["No results found."]
    except Exception as e:
        return [f"Error executing query: {str(e)}"]

# Define SQL conversion prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The database has the following schema:
    
    Table: Employee (ID, Name, DepartmentID, HireDate, Salary, ManagerID)
    Table: Departments (ID, Name, ManagerID)
    
    Example Queries:
    - "Show me all employees in the IT department." 
      SQL: SELECT * FROM Employee WHERE DepartmentID = (SELECT ID FROM Departments WHERE Name='IT');
    - "Who is the manager of the HR department?"
      SQL: SELECT Name FROM Employee WHERE ID = (SELECT ManagerID FROM Departments WHERE Name='HR');
    - "List all employees hired after 2020-01-01."
      SQL: SELECT * FROM Employee WHERE HireDate > '2020-01-01';
    - "What is the total salary expense for the Sales department?"
      SQL: SELECT SUM(Salary) FROM Employee WHERE DepartmentID = (SELECT ID FROM Departments WHERE Name='Sales');
    
    The SQL output should not contain ``` or the word 'SQL'.
    """
]

# Streamlit App UI
st.set_page_config(page_title="SQL Chat Assistant")
st.header("Chat Assistant for SQLite Database")

question = st.text_input("Enter your query:", key="input")
submit = st.button("Ask")

if submit:
    sql_query = get_gemini_response(question, prompt)
    response = read_sql_query(sql_query, "company.db")
    st.subheader("Response:")
    for row in response:
        st.write(row)