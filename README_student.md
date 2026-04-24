# MLOps Nginx Exam

## Structure du projet
```sh
. 
├── Makefile
├── README.md
├── README_student.md
├── data
│   └── tweet_emotions.csv
├── deployments
│   ├── nginx
│   │   ├── Dockerfile
│   │   ├── certs
│   │   │   ├── nginx.crt
│   │   │   └── nginx.key
│   │   └── nginx.conf
│   └── prometheus
│       └── prometheus.yml
├── docker-compose.yml
├── model
│   └── model.joblib
├── src
│   ├── api
│   │   ├── requirements.txt
│   │   ├── v1
│   │   │   ├── Dockerfile
│   │   │   └── main.py
│   │   └── v2
│   │       ├── Dockerfile
│   │       └── main.py
│   └── gen_model.py
└── tests
    └── run_tests.sh
```
## Démarrage

### 1. Lancer le projet
```bash
make start-project
```

### 2. Arrêter le projet
```bash
make stop-project
```

### 3. Régénérer le modèle
```bash
make new-model
```

### 4. Lancer les tests
```bash
make test
```

## Services disponibles

| Service | URL |
|---|---|
| API (via Nginx) | https://localhost/predict |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

## Credentials

| Service | Utilisateur | Mot de passe |
|---|---|---|
| API `/predict` | `admin` | `admin` |
| Grafana | `admin` | `admin` |