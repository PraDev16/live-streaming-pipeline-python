import pyodbc

# DB connection
server = r"(localdb)\MSSQLLocalDB"
database = "BikeStores"

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Trusted_Connection=yes;"
)

cursor = conn.cursor()

# Open text file
with open(r"C:\Users\d.pranathi\Desktop\hw_training\live_streaming_project\products_stream.txt", "r") as file:
    for line in file:
        product_id, product_name, category = line.strip().split(",")

        cursor.execute("""
            INSERT INTO stream_products (product_id, product_name, category)
            VALUES (?, ?, ?)
        """, int(product_id), product_name, category)

conn.commit()
conn.close()

print("All records inserted successfully!")