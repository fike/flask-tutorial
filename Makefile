PHONY: build up

migrate: export FLASK_APP = flaskr
migrate: export FLASK_ENV = development
init-db: export FLASK_APP = flaskr
init-db: export FLASK_ENV = development
gen-migrate: export FLASK_APP = flaskr
gen-migrate: export FLASK_ENV = development

build:
	docker-compose -f deployments/docker-compose.yaml up --build

up: down 
	docker-compose -f deployments/docker-compose.yaml up

down:
	docker-compose -f deployments/docker-compose.yaml down

down-db:
	docker-compose -f deployments/docker-compose.yaml stop db

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
	docker-compose -f deployments/docker-compose.yaml run --entrypoint 'coverage run -m pytest' flaskr
	docker-compose -f deployments/docker-compose.yaml run --entrypoint 'coverage report' flaskr
	docker-compose -f deployments/docker-compose.yaml run --entrypoint 'coverage html' flaskr

	# docker-compose -f deployments/docker-compose.yaml up -d db
local-test:
	coverage run -m pytest
	coverage report
	coverage html
	
logs:
	docker-compose -f deployments/docker-compose.yaml logs -f