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

    datum = input("Datum: ")
    land = input("Land: ")
    stadt = input("Stadt: ")

    val = f'"{datum}", "{land}", "{stadt}"'
    sql = f'INSERT INTO konzerte VALUES ({val})'



# INSERT-Anweisung korrekt formulieren

    cursor.execute(sql)

# Testabfrage: Vorhandene Datenbanken anzeigen
cursor.execute('SELECT name FROM sys.databases')
for db in cursor:
    print(db)
