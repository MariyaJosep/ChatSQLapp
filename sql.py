import sqlite3

def create_database():
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()
    
    # Create Departments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Departments (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT UNIQUE,
            ManagerID INTEGER
        )
    """)
    
    # Create Employee table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            DepartmentID INTEGER,
            HireDate TEXT,
            Salary REAL,
            ManagerID INTEGER,
            FOREIGN KEY (DepartmentID) REFERENCES Departments(ID),
            FOREIGN KEY (ManagerID) REFERENCES Employee(ID)
        )
    """)
    
    # Insert Departments (Ignore duplicate entries)
    departments = [("IT", 1), ("HR", 2), ("Sales", 3), ("Finance", 4)]
    for dept in departments:
        try:
            cursor.execute("INSERT INTO Departments (Name, ManagerID) VALUES (?, ?)", dept)
        except sqlite3.IntegrityError:
            pass  # Ignore duplicate entries
    
    # Insert Employees
    employees = [
        ("Alice", 1, "2021-06-15", 70000, None),
        ("Bob", 2, "2020-03-20", 65000, None),
        ("Charlie", 3, "2019-07-22", 72000, None),
        ("David", 4, "2022-01-10", 68000, None)
    ]
    
    cursor.executemany("INSERT INTO Employee (Name, DepartmentID, HireDate, Salary, ManagerID) VALUES (?, ?, ?, ?, ?)", employees)
    
    connection.commit()
    connection.close()

def print_all_data():
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()
    
    print("Departments Table:")
    for row in cursor.execute("SELECT * FROM Departments"):
        print(row)
    
    print("\nEmployee Table:")
    for row in cursor.execute("SELECT * FROM Employee"):
        print(row)
    
    connection.close()

if __name__ == "__main__":
    create_database()
    print_all_data()
