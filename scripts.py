import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch and print the result
tables = cursor.fetchall()
for table in tables:
    print(table[0])

# Close the connection
conn.close()
