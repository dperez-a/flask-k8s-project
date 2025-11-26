# flask-k8s-project
Full-stack Flask application deployed on Kubernetes with MySQL database, backend API, frontend web interface, and Nginx reverse proxy. Demonstrates container orchestration, persistent storage, and service communication in K8s.
# Flask App on Kubernetes

Full-stack application with Flask backend/frontend, MySQL database, and Nginx reverse proxy deployed on Kubernetes.

## Architecture

```
Nginx (NodePort 30000) → Frontend → Backend → MySQL
```

## Quick Start

### 1. Build Docker Images

```bash
# Backend
cd backend
docker build -t flasker/api:latest .

# Frontend
cd ../frontend
docker build -t flasker/frontend:latest .
```

### 2. Deploy to Kubernetes

```bash
cd k8s

# Deploy MySQL
kubectl apply -f mysql-deployment.yml

# Wait for MySQL pod to be ready
kubectl get pods -w

# Configure MySQL database
kubectl exec -it  -- sh
mysql -u root -prootpassword

# Run these SQL commands:
CREATE USER 'appuser'@'%' IDENTIFIED BY 'apppassword';
GRANT ALL PRIVILEGES ON *.* TO 'appuser'@'%';
CREATE DATABASE test_db;
USE test_db;
CREATE TABLE message (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(255) NOT NULL);
INSERT INTO message (text) VALUES ('hola mundo');
EXIT;

# Deploy remaining services
kubectl apply -f backend-deployment.yml
kubectl apply -f frontend-deployment.yml
kubectl apply -f nginx-deployment.yml
```

### 3. Access the Application

```bash
# Get Minikube IP
minikube ip

# Access in browser
http://:30000

# Or use port-forward
kubectl port-forward service/nginx-service 8080:80
# http://localhost:8080
```

## Verify Deployment

```bash
# Check all resources
kubectl get all

# Check specific components
kubectl get pods
kubectl get services
kubectl get pvc

# View logs
kubectl logs -l app=backend
kubectl logs -l app=frontend
```

## Components

- **MySQL**: Database with persistent storage (1Gi PVC)
- **Backend**: Flask API (port 5000) - 2 replicas
- **Frontend**: Flask web interface (port 80) - 2 replicas
- **Nginx**: Reverse proxy exposed on NodePort 30000

## Cleanup

```bash
kubectl delete -f k8s/
kubectl delete pvc mysql-pvc
```

## Tech Stack
