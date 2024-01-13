import psycopg2

# connecting to PostgreSQL database using the connect() function of the psycopg2 module
# connect() function creates a new database session and returns a new instance of the connection class.
conn = psycopg2.connect(dbname="ID_history", user="postgres", password="postgres", port="5432")
print('Connection is successful')

cursor = conn.cursor()

conn.autocommit = True

conn.commit()

cursor.close()
conn.close()
