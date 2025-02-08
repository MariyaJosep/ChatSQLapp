# ChatSQLapp

 This chat assistant that interacts with an SQLite database to answer user queries.
 Here I used Database named company, with 2 Tables: Employee and Departments.
 I'm Trying to developing an end to end LLm application using Google Gemini Pro where we will create Text To SQL LLM App  and later retrieving query from sql database
 Agenda:
 SQL LLM Application.
 Prompt---> LLM---> GeminiPro---> Query---> SQL Database---> Response
 Implementation:
 1. SQL LITE---> Insert some records---> Python Programing
 2. LLM Application---> Gemini Pro---> SQL Database

How to run:
1. Run sql.py to confirm the records are created successfully: python sql.py
2. Run Streamlit app: streamlit run app.py

 Supported Queries: 
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


    
