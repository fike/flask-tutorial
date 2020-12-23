PHONY: build up

build:
	docker-compose -f deployments/docker-compose.yaml up --build

up: down 
	docker-compose -f deployments/docker-compose.yaml up

down:
	docker-compose -f deployments/docker-compose.yaml down

down-db:
	docker-compose -f deployments/docker-compose.yaml down db

clean:
	docker-compose -f deployments/docker-compose.yaml down -v --rmi all

up-db:
	docker-compose -f deployments/docker-compose.yaml up -d db

migrate: up-db
	sleep 2
	docker-compose -f deployments/docker-compose.yaml run --entrypoint 'flask db upgrade' flaskr

gen-migrate: up-db
	sleep 2
	docker-compose -f deployments/docker-compose.yaml run --entrypoint 'flask db migrate' flaskr

init-db: up-db
	sleep 2
	docker-compose -f deployments/docker-compose.yaml run --entrypoint 'flask db init' flaskr

test:
	docker-compose -f deployments/docker-compose.yaml up -d db
	docker-compose -f deployments/docker-compose.yaml exec flaskr coverage run -m pytest
	docker-compose -f deployments/docker-compose.yaml exec flaskr coverage report
	docker-compose -f deployments/docker-compose.yaml exec flaskr coverage html
	
logs:
	docker-compose -f deployments/docker-compose.yaml logs -f