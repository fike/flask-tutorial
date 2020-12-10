PHONY: build up

migrate: export FLASK_APP = flaskr
migrate: export FLASK_ENV = development

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
	flask db upgrade
	flask db migrate

test:
	docker-compose -f deployments/docker-compose.yaml up -d db
	coverage run -m pytest
	coverage report
	coverage html
	
logs:
	docker-compose -f deployments/docker-compose.yaml logs -f