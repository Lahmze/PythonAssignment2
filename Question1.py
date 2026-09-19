import sqlite3

def main():
    connection = sqlite3.connect('question.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, department TEXT NOT NULL, email TEXT, salary REAL)''')
employees_data = [('James Moyo', 'Sales', 6000),('Lameck Muzenda', 'Production', 16000), ('Takudzwa Rimbi', 'Security', 3000), ('Gina Saibet', 'Marketing', 6500),]

cursor.executemany('INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)', employees_data)
connection.commit()

cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()

print(f"{'ID':<6}{'Name':<30}{'Department':<30}{'Salary':<100}")
print("-"*50)
for row in rows:
    id_, name, department, salary = row
    print(f'{id_:<6}{name:<30}{department:<30}{salary:<100}')

# retrieve with filter
cursor.execute('SELECT name, salary FROM employees where department = ?', (Production,))
artisans = cursor.fetchall()
print("\nProduction department employees:")
for name, salary in artisans:
    print(f" {name}: ${salary:,.2f}")

connection.close()

if __name__ == "__main__":
    main()