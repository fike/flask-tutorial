PHONY: build up

ANT_HOME := /usr/local/ant 

DC_EXEC := docker-compose

DC_DIR := deployments

DC_FLASKR := docker-compose.yaml
DC_JAEGER := docker-compose-jaeger.yaml

build:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) up --build --no-start --remove-orphans

up:  
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) up --remove-orphans

down:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) down

down-db:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) stop db

down-jaeger:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_JAEGER) down

clean: down-jaeger down
	docker system prune -f

up-db:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) up -d db

up-jaeger:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_JAEGER) up --remove-orphans 

up-all:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_JAEGER) -f $(DC_DIR)/$(DC_FLASKR) up --remove-orphans 

migrate: up-db
	sleep 2
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) run --entrypoint 'flask db upgrade' flaskr

gen-migrate: up-db
	sleep 2
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) run --entrypoint 'flask db migrate' flaskr

init-db: up-db
	sleep 2
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) run --entrypoint 'flask db init' flaskr

test:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) run --entrypoint 'coverage run -m pytest' flaskr
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) run --entrypoint 'coverage report' flaskr
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) run --entrypoint 'coverage html' flaskr

local-test:
	coverage run -m pytest
	coverage report
	coverage html
	
logs:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_FLASKR) -f $(DC_DIR)/$(DC_JAEGER) logs -f