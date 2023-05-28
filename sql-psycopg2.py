import psycopg2

#connect to relevant database

connection = psycopg2.connect(database="nameofdatabase")

#build a cursor object of the database

cursor = connection.cursor()

#Queries to be inserted here. AFTER the cursor variable but BEFORE the results are fetched
#Using execute method

cursor = cursor.execute('SELECT ** FROM ""')

#fetch the results (multiple)

results = cursor.fetchall()

#fetch the results (single)

# results = cursor.fetchone()

#close the connection

connection.close()

#print results

for result in results:
    print(result)