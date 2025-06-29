get-airflow:
	docker pull apache/airflow:slim-latest-python3.9
init:
	mkdir -p ./dags ./logs ./plugins ./data
	touch .env
	echo "AIRFLOW_UID=$(id -u)" > .env
	echo "AIRFLOW_GID=0" >> .env
	docker compose up

up:
	docker compose up

down:
	docker-compose down --volumes --remove-orphans

clean:
	rm -rf dags/__pycache__ logs/* plugins/* data/* .env
get-credentials:
	docker exec -it airflow-airflow-1 cat /opt/airflow/simple_auth_manager_passwords.json.generated