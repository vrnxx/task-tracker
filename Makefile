up:
	docker-compose -f docker-compose-dev.yaml up -d
down-db:
	docker-compose -f docker-compose-dev.yaml down && docker network prune --force
