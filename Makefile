COMPOSE_FILE = docker-compose.yml
IMAGE_TAG ?= main
ENV ?= local

COMPOSE_FILE = docker-compose.yml
ifeq ($(ENV), ci)
    COMPOSE_FILE += -f docker-compose.ci.yml
endif

up:
	docker compose -f $(COMPOSE_FILE) pull backend
	docker compose -f $(COMPOSE_FILE) up -d
	docker compose -f $(COMPOSE_FILE) wait db-seed
down:
	docker compose -f $(COMPOSE_FILE) down -v --remove-orphans
logs:
	docker compose -f $(COMPOSE_FILE) logs
allure-report:
	allure generate allure-results -o allure-report --clean
rebuild: down up