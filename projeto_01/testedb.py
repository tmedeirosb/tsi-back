import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

cur.execute('INSERT INTO app1_agenda (nome, telefone) VALUES (?, ?)', ('João', 123456789))
cur.execute('INSERT INTO app1_agenda (nome, telefone) VALUES (?, ?)', ('Maria', 987654321))
cur.execute('INSERT INTO app1_agenda (nome, telefone) VALUES (?, ?)', ('José', 123456789))

con.commit()
con.close()