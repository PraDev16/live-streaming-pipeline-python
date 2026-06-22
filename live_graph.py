import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

server = r"(localdb)\MSSQLLocalDB"
database = "BikeStores"

fig, ax = plt.subplots(figsize=(6, 3))

def animate(i):
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    query = """
    SELECT category, COUNT(*) as count
    FROM stream_products
    GROUP BY category
    """

    df = pd.read_sql(query, conn)
    conn.close()

    ax.clear()
    ax.barh(df["category"], df["count"])
    ax.set_title("Live Bike Count by Category")
    ax.set_xlabel("Count")
    ax.set_ylabel("Category")

ani = FuncAnimation(fig, animate, interval=2000)
plt.tight_layout()
plt.show()