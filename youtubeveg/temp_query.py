import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT username FROM auth_user WHERE is_superuser=1;")
results = cursor.fetchall()
for row in results:
    print(row[0])
conn.close()