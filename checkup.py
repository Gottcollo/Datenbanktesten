import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=localhost;'
    'DATABASE=Tourplaner;'
    'UID=sa;'
    'PWD=Samu1234'
)
conn.autocommit = True
cursor = conn.cursor()

# Prüfen, ob die Tabelle existiert
cursor.execute("""
SELECT COUNT(*) 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME = 'konzerte'
""")
table_exists = cursor.fetchone()[0]

if table_exists == 0:
    print("❌ Tabelle 'konzerte' existiert NICHT.")
else:
    print("✅ Tabelle 'konzerte' existiert.")

    # Anzahl der Zeilen prüfen
    cursor.execute("SELECT COUNT(*) FROM konzerte")
    count = cursor.fetchone()[0]
    print(f"📦 Anzahl Einträge in 'konzerte': {count}")

    # Inhalt anzeigen, wenn was da ist
    if count > 0:
        cursor.execute("SELECT datum, land, stadt FROM konzerte")
        for row in cursor.fetchall():
            print(f"→ {row.datum} | {row.land} | {row.stadt}")
    else:
        print("⚠️ Tabelle ist leer.")
