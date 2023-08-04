up-db:
	docker-compose -f docker-compose-dev.yaml up -d
down-db:
	docker-compose -f docker-compose-dev.yaml down && docker network prune --force
start-app:
	python -m src
format:
	isort .
	black . --line-length=80
	flake8 . --count --show-source --statistics --max-line-length 80