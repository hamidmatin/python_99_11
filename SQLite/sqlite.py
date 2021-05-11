import sqlite3

def connect_db():
  con = sqlite3.connect('my-database.db')
  
  cur = con.cursor()

  # Create table
  # cur.execute('''CREATE TABLE stocks
  #              (id integer PRIMARY KEY DESC, date text, trans text, symbol text, qty real, price real)''')

  
  # Insert a row of data
  # cur.execute("INSERT INTO stocks VALUES (2, '2006-01-05','BUY','RHAT',100,35.14)")

  # Save (commit) the changes
  # con.commit()


  # Select all rows
  cur.execute('SELECT * FROM stocks')
  print(cur.fetchall())

  # We can also close the connection if we are done with it.
  # Just be sure any changes have been committed or they will be lost.
  con.close()