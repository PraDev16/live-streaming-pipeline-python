import pyodbc

server = r"(localdb)\MSSQLLocalDB"
database = "BikeStores"

try:
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT TOP 3 * FROM production.brands")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
    print("SUCCESS: Connected to BikeStores!")

except Exception as e:
    print("ERROR:")
    print(e)