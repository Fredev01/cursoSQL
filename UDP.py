"""
    importando el modulo 
"""
import sqlite3
import pandas as pd 

# funcion definida por el usuario
square = lambda n : n*n

"""
conn = sqlite3.connect("Northwind.db")
conn.create_function("square", 1, square)

# creando un cursor 
cursor = conn.cursor()
cursor.execute('''
               SELECT * FROM Products
               ''')
results = cursor.fetchall()
results_df = pd.DataFrame(results)
# guardar los cambios 
conn.commit()

# cerrar la consuta 
cursor.close()
# cerrar la conexion 
conn.close()

print(results_df)
"""

with sqlite3.connect("Northwind.db") as conn:
    conn.create_function("square", 1, square)
    cursor = conn.cursor()
    cursor.execute('SELECT *, square(Price) FROM Products WHERE Price > 0')
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)
    
print(results_df)
