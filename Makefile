run-project:
	# run project
	@echo "Grafana UI: http://localhost:3000"

test-api:
	curl -X POST "https://localhost/predict" \
     -H "Content-Type: application/json" \
     -d '{"sentence": "Oh yeah, that was soooo cool!"}' \
	 --user admin:admin \
     --cacert ./deployments/nginx/certs/nginx.crt;

# Effectue tous les tests
test:
	bash tests/run_tests.sh

# Build et lance tous les conteneurs
start-project:
	docker compose up -d --build

# Arrête et supprime tous les conteneurs
stop-project:
	docker compose down

new-model:
	docker compose --profile tools run --rm gen-model
	# Puis relancer les APIs (sans rebuild, le .joblib est mis à jour via volume)
	docker compose restart api-v1 api-v2