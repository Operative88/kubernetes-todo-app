# K8s Todo App

A full-stack Todo application built with Flask backend, vanilla JavaScript frontend, PostgreSQL database, and Kubernetes orchestration.

## Overview

This project demonstrates a containerized todo application that can be deployed locally using Docker Compose or in a Kubernetes cluster. The application allows users to create and manage their todo tasks with a simple, responsive web interface.

## Architecture

The application consists of three main components:

- **Backend**: Flask REST API that handles todo operations
- **Frontend**: Web-based user interface built with HTML and JavaScript
- **Database**: PostgreSQL for persistent data storage

```
Frontend (Nginx) -> Backend (Flask) -> PostgreSQL Database
```

## Prerequisites

### For Local Development
- Docker
- Docker Compose

### For Kubernetes Deployment
- Kubernetes cluster (v1.19+)
- kubectl command-line tool
- Docker registry access (for custom images)

## Installation

### Option 1: Local Development with Docker Compose

1. Clone the repository:
```bash
git clone <repository-url>
cd k8s-todo-app
```

2. Start the application:
```bash
docker-compose up -d
```

3. Access the application:
- Frontend: http://localhost:8080
- Backend API: http://localhost:5000

4. Stop the application:
```bash
docker-compose down
```

### Option 2: Kubernetes Deployment

#### Prerequisites
- Push your Docker images to a registry or use local images
- Update image references in the Kubernetes manifests if needed

#### Deployment Steps

1. Create a namespace (optional):
```bash
kubectl create namespace todo-app
```

2. Apply configuration:
```bash
kubectl apply -f k8s/config.yaml
```

3. Create persistent volume claim:
```bash
kubectl apply -f k8s/pvc.yaml
```

4. Deploy PostgreSQL:
```bash
kubectl apply -f k8s/postgres.yaml
```

5. Deploy backend service:
```bash
kubectl apply -f k8s/backend.yaml
```

6. Deploy frontend service:
```bash
kubectl apply -f k8s/frontend.yaml
```

7. Set up ingress:
```bash
kubectl apply -f k8s/ingress.yaml
```

8. Verify deployment:
```bash
kubectl get pods
kubectl get services
kubectl get ingress
```

## Project Structure

```
k8s-todo-app/
├── backend/                 # Flask backend application
│   ├── app.py             # Main Flask application
│   ├── Dockerfile         # Backend container configuration
│   └── requirements.txt    # Python dependencies
├── frontend/              # Web frontend
│   ├── index.html         # Frontend UI
│   └── Dockerfile         # Frontend container configuration
├── k8s/                   # Kubernetes manifests
│   ├── backend.yaml       # Backend Kubernetes deployment
│   ├── frontend.yaml      # Frontend Kubernetes deployment
│   ├── postgres.yaml      # PostgreSQL Kubernetes deployment
│   ├── config.yaml        # Configuration and ConfigMaps
│   ├── ingress.yaml       # Ingress configuration
│   └── pvc.yaml           # Persistent Volume Claim
├── docker-compose.yml     # Docker Compose configuration
├── init.sql              # Database initialization script
└── README.md             # This file
```

## API Endpoints

### Get All Todos
```
GET /api/todos
```

Response:
```json
[
  "Buy groceries",
  "Complete project",
  "Review code"
]
```

### Add Todo
```
POST /api/todos
Content-Type: application/json

{
  "task": "New todo item"
}
```

Response:
```json
{
  "message": "Task added successfully"
}
```

## Environment Variables

### Backend
- `DB_HOST` - Database host (default: `db`)
- `DB_USER` - Database user (default: `postgres`)
- `DB_PASSWORD` - Database password (default: `mysecretpassword`)
- `DB_NAME` - Database name (default: `tododb`)

## Database Schema

The application uses a simple `todos` table:

```sql
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    task VARCHAR(255) NOT NULL
);
```

## Development

### Backend Development

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables and run the application:
```bash
set DB_HOST=localhost
python app.py
```

### Frontend Development

The frontend is a static HTML/JavaScript application. Open `frontend/index.html` in a browser to view the UI.

## Building Docker Images

### Build and tag images
```bash
docker build -t your-registry/todo-backend:latest ./backend
docker build -t your-registry/todo-frontend:latest ./frontend
```

### Push to registry
```bash
docker push your-registry/todo-backend:latest
docker push your-registry/todo-frontend:latest
```

## Troubleshooting

### Database Connection Issues
- Verify PostgreSQL is running: `docker-compose ps`
- Check database credentials in environment variables
- Ensure database initialization script (init.sql) executed successfully

### Frontend Cannot Reach Backend
- Verify backend service is running
- Check CORS configuration in Flask app
- Verify API endpoint URL in frontend JavaScript

### Kubernetes Deployment Issues
- Check pod status: `kubectl describe pod <pod-name>`
- View logs: `kubectl logs <pod-name>`
- Verify resources: `kubectl get events`

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
