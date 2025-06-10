import pyodbc
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=localhost;'
    'DATABASE=master;'
    'UID=sa;'
    'PWD=Samu1234' 
    )
cursor = conn.cursor()
#cursor.execute('SELECT * FROM sys.databases')
#for DB in cursor.fetchall():
 #   print(DB[0])
#cursor.execute("SELECT * FROM sys.tables where name = 'Bankai'")
#for table in cursor.fetchall():
 #   print(table[0])
cursor.execute("SELECT name FROM sys.tables")
print("Tabellen in der Datenbank:")
for row in cursor.fetchall():
    print(" -", row.name)
 
cursor.execute("SELECT * FROM Bankai.dbo.Kunden")
print("\nInhalt der Tabelle 'Kunden':")
columns = [column[0] for column in cursor.description]
rows = cursor.fetchall()
 
for row in rows:
    print(dict(zip(columns, row)))
 
cursor.close()
conn.close()