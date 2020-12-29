import sqlite3
conn = sqlite3.connect('Apexmaps.db')

c = conn.cursor()

c.execute('''CREATE TABLE champions (
            champions text
            )''')

conn.commit()

conn.close()