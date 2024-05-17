build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

test:
	docker-compose run --rm app poetry run pytest


restart: 
	down up

coverage:
	docker-compose run --rm app poetry run pytest --cov=app --cov-report=term-missing --cov-report=html
