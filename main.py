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



sql = """ 
INSERT INTO konzerte VALUE (
    '2017-11-11',
    'Israel',
    'Haifa'
    )

"""
cursor.execute(sql)

cursor.execute('SELECT name FROM sys.databases')
for db in cursor:
    print(db)