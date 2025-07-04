from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pendulum
import pandas as pd
import requests
from dateutil import parser
from pathlib import Path

# -------------------------------
# Configuration des localisations
# -------------------------------
city_coords = {
    "Paris":  {"lat": 48.85, "lon": 2.35},
    "London": {"lat": 51.51, "lon": -0.13},
    "Berlin": {"lat": 52.52, "lon": 13.41},
    "Madrid": {"lat": 40.42, "lon": -3.70},
}

# -------------------------------
# Étape A : Collecte météo
# -------------------------------
def fetch_weather():
    collected = {}
    for city, location in city_coords.items():
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={location['lat']}&longitude={location['lon']}&current_weather=true"
        )
        try:
            res = requests.get(url, timeout=10)
            res.raise_for_status()
            weather = res.json().get("current_weather", {})
            collected[city] = {
                "temp": weather.get("temperature"),
                "wind": weather.get("windspeed"),
                "code": weather.get("weathercode"),
                "humidity": None  # Donnée fictive
            }
        except Exception as e:
            print(f"❌ Erreur lors de la collecte pour {city}: {e}")
            collected[city] = {"temp": None, "wind": None, "code": None, "humidity": None}
    return collected

# -------------------------------
# Étape B : Transformation
# -------------------------------
def process_data(ti):
    raw = ti.xcom_pull(task_ids="collect_task")
    now = datetime.now(pendulum.timezone("Europe/Paris"))
    run_day = now.strftime("%Y-%m-%d")
    formatted = []

    for city, metrics in raw.items():
        formatted.append({
            "ville": city,
            "horodatage": now.isoformat(),
            "temperature_C": metrics.get("temp"),
            "vent_kmh": metrics.get("wind"),
            "code_meteo": metrics.get("code"),
            "humidite": metrics.get("humidity"),
            "ref": f"{city}_{run_day}"
        })

    df = pd.DataFrame(formatted)
    ti.xcom_push(key="clean_data", value=df.to_dict(orient="records"))

# -------------------------------
# Étape C : Sauvegarde CSV locale
# -------------------------------
def save_output(ti):
    dataset = ti.xcom_pull(key="clean_data", task_ids="format_task")
    df = pd.DataFrame(dataset)

    # Chemin vers le fichier CSV
    file_path = Path("data/meteo_archive.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"📁 Le fichier CSV sera sauvegardé ici : {file_path.resolve()}")

    if file_path.exists():
        existing = pd.read_csv(file_path)
        # Normalisation des dates
        df["horodatage"] = df["horodatage"].apply(lambda x: parser.isoparse(x).isoformat())
        existing["horodatage"] = existing["horodatage"].apply(lambda x: parser.isoparse(x).isoformat())
        df["jour"] = df["horodatage"].apply(lambda x: parser.isoparse(x).date())
        existing["jour"] = existing["horodatage"].apply(lambda x: parser.isoparse(x).date())
        total = pd.concat([existing, df], ignore_index=True)
        total.drop_duplicates(subset=["ville", "jour"], keep="last", inplace=True)
    else:
        df["jour"] = df["horodatage"].apply(lambda x: parser.isoparse(x).date())
        total = df

    total.drop(columns=["ref", "jour"], inplace=True, errors="ignore")
    total.to_csv(file_path, index=False)

# -------------------------------
# Définition du DAG
# -------------------------------
with DAG(
    dag_id="daily_meteo_etl",
    schedule="0 7 * * *",  # Chaque jour à 07:00 UTC
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["meteo"],
) as dag:

    collect_task = PythonOperator(
        task_id="collect_task",
        python_callable=fetch_weather
    )

    format_task = PythonOperator(
        task_id="format_task",
        python_callable=process_data
    )

    export_task = PythonOperator(
        task_id="export_task",
        python_callable=save_output
    )

    collect_task >> format_task >> export_task
