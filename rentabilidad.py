import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


conn: str = sqlite3.connect("Northwind.db")
# Obteniendo los 10 productos mas rentables
query: str = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC 
    LIMIT 10 
'''

top_products = pd.read_sql_query(query, conn)
# creando un grafico
top_products.plot(x="ProductName", y="Revenue", kind="bar",
                  figsize=(10, 5), legend=False)
# configurando un grafico
plt .title("10 Productos mas rentables")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.show()

# Obteniendo los 10 productos mas rentables
query2: str = '''
    SELECT FirstName || " " || LastName AS Employee, COUNT(*) AS total
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID 
    ORDER BY total ASC 
    LIMIT 3  
'''

top_employees = pd.read_sql_query(query2, conn)
top_employees.plot(x="Employee", y="total", kind="bar",
                   figsize=(10, 5), legend=False)

# configurando un grafico
plt.title("10 Empleados mas efectivos")
plt.xlabel("Empleado")
plt.ylabel("Total vendido")
plt.xticks(rotation=45)
plt.show()
