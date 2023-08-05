up-db:
	docker-compose -f docker-compose-dev.yaml up -d
down-db:
	docker-compose -f docker-compose-dev.yaml down
up-test_db:
	docker-compose -f docker-compose-test.yaml up -d
down-test_db:
	docker-compose -f docker-compose-test.yaml down
start-app:
	python -m src
format:
	isort .
	black . --line-length=80
	flake8 . --count --show-source --statistics --max-line-length 80

#&& docker network prune --force