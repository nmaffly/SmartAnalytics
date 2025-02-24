import sqlite3
import random
import string

conn = sqlite3.connect('./sqlite/dummy_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    email TEXT
)
''')

def random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def random_email(name):
    domains = ['example.com', 'test.com', 'mail.com']
    return f"{name}@{random.choice(domains)}"

for _ in range(100):
    name = random_string()
    age = random.randint(18, 70)
    email = random_email(name)
    cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))

conn.commit()
conn.close()

print("Dummy data has been inserted into the database.")