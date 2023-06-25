import sqlite3

# Create a SQLite database and establish a connection
conn = sqlite3.connect('bakarwal_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL statement to create a table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS information (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        arrival_date TEXT,
        goats INTEGER,
        aadhar_id INTEGER,
        relationship_id TEXT,        
        relationship TEXT
        
    )
'''
cursor.execute(create_table_query)




"""
# Insert data into the table
insert_data_query = '''
INSERT INTO information (name,age,gender,arrival_date,goats,aadhar_id,relationship_id,relationship) VALUES (?,?,?,?,?,?,?,?)
'''
user_data = [
    ('John Doe',25,"male","sfff",44,"fsfs","fsff","ererre"),
    
]
cursor.executemany(insert_data_query, user_data)

# Commit the changes to the database
conn.commit()

# Read data from the table
select_data_query = '''
SELECT * FROM information
'''
cursor.execute(select_data_query)

# Fetch all the rows as a list of tuples
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
"""
# Close the cursor and the database connection
cursor.close()
conn.close()
