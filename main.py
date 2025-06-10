import pyodbc
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=localhost;'
    'DATABASE=Tourplaner;'
    'UID=sa;'
    'PWD=Samu1234' 
    )

conn.autocommit = True  # Enable autocommit mode
cursor = conn.cursor()



insert_sql = """
INSERT INTO konzerte (datum, land, stadt)
VALUES (?, ?, ?)
"""
cursor.execute(insert_sql, ('2017-11-11', 'Israel', 'Haifa'))

cursor.execute('SELECT name FROM sys.databases')
for db in cursor:
    print(db)