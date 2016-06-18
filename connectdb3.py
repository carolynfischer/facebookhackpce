import sqlite3

sqlite_file ='test.db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
table_name = 'entries'
c.execute('SELECT * FROM entries')
all_rows = c.fetchall()
print('1):', all_rows)
name=('Promila',)
score = -1

c.execute("SELECT score FROM entries where user =?",name)

all_rows = c.fetchall()
print('1):', all_rows)
print all_rows[0][0]
print score

score = 1
name1 = 'Promila'
c.execute("update entries set score =? where user =?",[score, name1])

c.execute("SELECT score FROM entries where user =?",name)

all_rows = c.fetchall()
print('1):', all_rows)
print all_rows[0][0]
print score

score = 2
name1 = 'Erin'
c.execute("insert into  entries(user,score,last_post) values (?, ?,?)",[name1,score,"05/14/2016"])
c.execute("SELECT * from entries")

all_rows = c.fetchall()
print('1):', all_rows)

conn.close()
