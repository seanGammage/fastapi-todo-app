# Very unnoffical README

### Start the app with Kubernetes
- Once all the kubernetes objects are deployed, run `minikube service fastapi-service`

### Start the app locally with Docker
1. Run `Docker-compose up`
2. Access the swagger docs at `http://localhost:8000/docs`

### Stop the app locally with Docker
- Run `docker-compose down`
- To stop and remove volume, run `http://localhost:8000/docs`

### Virutal Environment
- Create if needed: `python -m venv venv`
- Activate it: `source venv/bin/activate`
- Install the dependencies: `pip install -r requirements.txt`

### Alembic Migrations
1. Make sure the model is imported in the alembic .env file
2. Make sure to run `docker-compose up` so the db is up and running
2. run `alembic revision --autogenerate -m "<some message here>"`
3. Apply changes `alembic upgrade head`