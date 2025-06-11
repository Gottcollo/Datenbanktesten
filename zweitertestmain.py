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

def insert_concert_from_user_input():
    datum = input("Datum (YYYY-MM-DD): ")
    land = input("Land: ")
    stadt = input("Stadt: ")

    sql = 'INSERT INTO konzerte (datum, land, stadt) VALUES (?, ?, ?)'
    cursor.execute(sql, (datum, land, stadt))
    print("Eintrag erfolgreich hinzugefügt.")

# Funktion aufrufen
insert_concert_from_user_input()

# Testabfrage: Vorhandene Datenbanken anzeigen
cursor.execute('SELECT name FROM sys.databases')
for db in cursor:
    print(db)
