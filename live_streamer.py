import time
import pyodbc
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

server = r"(localdb)\MSSQLLocalDB"
database = "BikeStores"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "products_stream.txt")


# Object Oriented Python
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == FILE_PATH:
            print("File changed! Updating database...")
            load_file_to_db()


def load_file_to_db():
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    cursor = conn.cursor()

    try:
        # Delete old data (but don't commit yet)
        cursor.execute("DELETE FROM stream_products")

        # Reload file data
        with open(FILE_PATH, "r") as file:
            for line in file:
                product_id, product_name, category = line.strip().split(",")

                cursor.execute("""
                    INSERT INTO stream_products (product_id, product_name, category)
                    VALUES (?, ?, ?)
                """, int(product_id), product_name, category)

        # Commit only if everything succeeds
        conn.commit()
        print("Database updated successfully!")

    except Exception as e:
        # Rollback if anything fails
        conn.rollback()
        print("Transaction failed. Rolled back changes.")
        print("Error:", e)

    finally:
        conn.close()


event_handler = FileChangeHandler()
observer = Observer()

folder_to_watch = os.path.dirname(FILE_PATH)
observer.schedule(event_handler, folder_to_watch, recursive=False)
observer.start()

print("Watching file for changes...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()