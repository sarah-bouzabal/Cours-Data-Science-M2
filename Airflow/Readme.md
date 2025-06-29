
# 🌀 Apache Airflow Docker Lab

Welcome to the **Airflow Docker Lab**! This lab will help you learn how to:
- Install and run Apache Airflow using Docker
- Access the Airflow web interface
- Write and schedule your first DAGs (Directed Acyclic Graphs)
- Manage task execution and branching
- Build a simple real-world ETL pipeline

---

## Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/)
- A UNIX shell (Linux, macOS, or WSL on Windows)

---

## Step 1: Setup the Lab

### 🏗️ 1. Clone or Download the Repository

You are inside the Airflow repository, use the Makefile for setup. Pulls the Apache Airflow Docker image:

```bash
make get-airflow
````

---

### 🧪 2. Initialize the Airflow Environment

```bash
make init
```

**What this does:**

* Creates folders: `dags/`, `logs/`, `plugins/`, `data/`
* Generates `.env` with your user ID
* Initializes the Airflow metadata database

---

### 🚀 3. Start Airflow Services

```bash
make up
```

Wait for logs to stabilize and confirm that the **scheduler** and **webserver** are running.

---

## 🌐 Step 2: Access the Airflow UI

Open your browser and navigate to:

👉 [http://localhost:8080](http://localhost:8080)

Get Credentials:
```bash
make get-credentials
```

Login using logged username and password:
```json
{"admin": "fdm9NbWagZMnzGnb"}
```


🔍 **Explore the UI:**

* DAGs list
* Graph View & Tree View
* Task Instance logs
* Admin panel (Connections, Variables)

---

## 🧪 Step 3: Run Your First DAGs

All DAGs are stored in the `dags/` folder and will automatically appear in the UI.

### 1️⃣ `hello_world.py`

* ✅ Purpose: Introduce a basic Python task
* 📍 Action: Trigger manually and inspect logs
* 💡 Takeaway: Understand basic DAG and task structure

```python
dag_id = "hello_world"
```

---

### 2️⃣ `multi_step_pipeline.py`

* ✅ Purpose: Simulate a simple ETL pipeline
* 📍 Action: Trigger DAG, explore task dependencies in Graph View
* 💡 Takeaway: Learn how to chain tasks using `>>`

```python
extract >> transform >> load
```

---

### 3️⃣ `conditional_pipeline.py`

* ✅ Purpose: Demonstrate branching logic using `BranchPythonOperator`
* 📍 Action: Trigger multiple runs to observe random paths
* 💡 Takeaway: Understand how dynamic task selection works

```python
choose_path() -> path_a or path_b -> join
```

---

### 4️⃣ `real_pipeline.py`

* ✅ Purpose: Execute a mini real-world data pipeline
* 📍 Action: Downloads NYC taxi data → Cleans it with Pandas
* 💡 Takeaway: Apply Python scripts in DAGs, use external packages

```python
download_csv >> clean_csv
```

---

## 🧹 Step 4: Clean Up

When you’re done:

```bash
make down
```

To clean temporary files and logs:

```bash
make clean
```

---

## 📝 Summary: What You’ve Learned

| Concept                    | Demonstrated In                   |
| -------------------------- | --------------------------------- |
| DAG structure              | `hello_world.py`                  |
| Task dependencies          | `multi_step_pipeline.py`          |
| Conditional branching      | `conditional_pipeline.py`         |
| Real-world ETL integration | `real_pipeline.py`                |
| Web UI monitoring          | All DAGs                          |
| Docker-based setup         | `Makefile`, `docker-compose.yaml` |

---

## 💡 Next Steps (Optional Challenges)

* Add a task that sends an email on completion
* Use `FileSensor` to wait for a file to appear before running
* Modify `real_pipeline.py` to upload cleaned data to a database

