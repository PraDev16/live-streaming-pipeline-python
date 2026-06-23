Live Streaming Data Pipeline using Python and SQL Server


ABOUT THE PROJECT:
This project is a simple simulation of a real-time data engineering pipeline built using Python and SQL Server.

The idea was to mimic how streaming systems work in industry. Instead of manually loading data into a database, I created a pipeline that continuously watches a text file for changes. Whenever new bike product records are added or updated in the file, the pipeline automatically detects the change, updates SQL Server, and refreshes a live graph.

This helped me understand core data engineering concepts like streaming, ETL, event-driven processing, and live visualization.


ARCHITECTURE:
Text File → Watchdog → Python ETL → SQL Server → Live Graph

TECH STACK
- Python  
- SQL Server (BikeStores database)  
- pyodbc  
- watchdog  
- Matplotlib  
- Git & GitHub  

HOW THE PIPELINE WORKS:

1. `live_streamer.py` continuously monitors `products_stream.txt`
2. When the file is modified, an event is triggered using Watchdog
3. Python reads the updated file
4. Data is transformed and loaded into SQL Server
5. `live_graph.py` fetches the latest data and updates the graph in real time

IN SHORT:

**File change → Event detected → Database updated → Graph refreshed**

PROJECT FILES:

- `live_streamer.py` → Main streaming pipeline  
- `live_graph.py` → Live graph visualization  
- `products_stream.txt` → Input data source  
- `setup.sql` → SQL script to create required table  

---

DATABASE SETUP:

Run the SQL script below before starting the project:

```sql
setup.sql
```

This creates the `stream_products` table used by the pipeline.

---

HOW TO RUN THIS PROJECT:

### Terminal 1 — Start Streaming Pipeline

```bash
python live_streamer.py
```

Expected output:

```txt
Watching file for changes...
```

---

### Terminal 2 — Start Live Graph

```bash
python live_graph.py
```

This opens the visualization window.

---

### Trigger Streaming

Open:

```txt
products_stream.txt
```

Add or modify records and save the file.

The database and graph will update automatically.

FEATURES:
✔ Real-time file monitoring  
✔ Event-driven ingestion  
✔ ETL pipeline using Python  
✔ Transaction-safe database updates  
✔ Live graph visualization  

CHALLENGES SOLVED:
During code review, I improved the project by:

- Replacing hardcoded absolute paths with relative paths  
- Adding transaction handling with rollback support  
- Removing redundant helper scripts  
- Cleaning project structure and documentation  

These changes made the pipeline cleaner and more production-friendly.

MY LEARNING:
This project gave me hands-on experience with:

- Batch vs Streaming systems  
- File system event handling  
- Python to SQL Server integration  
- ETL pipeline design  
- Real-time visualization  

It also helped me think more like a data engineer — not just making code work, but making it maintainable and production-ready.

---

FUTURE IMPROVEMENTS:

If I continue this project, I would like to add:

- Kafka for real streaming  
- Incremental loading instead of full reload  
- Cloud deployment  
- Dashboard using Power BI or Tableau  
