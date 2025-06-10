import pyodbc

# Verbindung zur MSSQL-Datenbank
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=localhost;'
    'DATABASE=Tourplaner;'
    'UID=sa;'
    'PWD=Samu1234'
)

conn.autocommit = True  # Autocommit aktivieren
cursor = conn.cursor()

# INSERT-Anweisung korrekt formulieren
sql = """
INSERT INTO konzerte (datum, land, stadt)
VALUES (?, ?, ?)
"""
cursor.execute(sql, ('2017-11-11', 'Israel', 'Haifa'))

# Testabfrage: Vorhandene Datenbanken anzeigen
cursor.execute('SELECT name FROM sys.databases')
for db in cursor:
    print(db)
