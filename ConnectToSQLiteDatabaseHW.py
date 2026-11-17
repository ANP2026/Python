import sqlite3
database= 'database.sqlite'
conn=sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd
tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
tables

conn.execute("""
    CREATE TABLE IF NOT EXISTS basketball(
        name TEXT,
        age INTEGER,
        team TEXT,
        points INTEGER
    );
""")
conn.commit()
print("Basketball table made succesfully")

conn.execute("""
    INSERT INTO basketball(name,age,team,points) VALUES
    ("Lebron", 42, "Pythons", 99),
    ("James", 33, "Lakers", 97),
    ("Micheal", 31, "Celtics", 100),
    ("Jackson", 44, "All-Stars", 92);
    """)
conn.commit()
print("Values inserted succesfully")
df = pd.read_sql("SELECT * FROM basketball;", conn)
print(df)