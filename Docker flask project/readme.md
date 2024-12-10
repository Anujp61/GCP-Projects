# Flask Application Deployment on Docker and GKE
## Overview
### This project demonstrates the deployment of a Flask-based web application:

- Locally using Docker for containerization.
- On Google Kubernetes Engine (GKE) for scalability and production-readiness.


## Features
- Dockerized Flask Application.
- Kubernetes Deployment: Leveraging GKE for high availability and scalability.
- Cloud-Native Practices: Use of container registries, LoadBalancer services, and autoscaling.
- Cost Optimization: Strategies for minimizing expenses on Google Cloud Platform (GCP).

## Technologies Used
- Flask: Python micro-framework for building web applications.
- Docker: For containerizing the application.
- Kubernetes: For orchestration and management of containers.
- GKE (Google Kubernetes Engine): Managed Kubernetes service by Google Cloud.
- Google Cloud Platform (GCP): Cloud infrastructure.

## Deployment Process
### 1. Local Deployment Using Docker
- Build the Docker Image:

```
docker build -t flask-app:v1 .
```
- Run the Container:

```
docker run -p 5000:5000 flask-app:v1
```

`Access the Application: Open the browser and navigate to http://localhost:5000.`

### 2. Deployment on GKE
- Create a GKE Cluster:
```
gcloud container clusters create flask-cluster --zone us-central1-a --num-nodes=3
```
![alt text](<images/Screenshot 2024-12-09 184923.png>)

![alt text](<images/Screenshot 2024-12-09 184659.png>)

- Configure kubectl:

```
gcloud container clusters get-credentials flask-cluster --zone us-central1-a
```
- Push Docker Image to Google Container Registry:
```
docker tag flask-app:v1 gcr.io/[project-id]/flask-app:v1
docker push gcr.io/[project-id]/flask-app:v1
```
![alt text](<images/Screenshot 2024-12-09 185001.png>)



- Deploy the Application:

- Create a Kubernetes Deployment and Service YAML file (k8s-deployment.yaml).
- Apply the configuration:

```
kubectl apply -f k8s-deployment.yaml
```
![alt text](<images/Screenshot 2024-12-09 184642.png>)
![alt text](<images/Screenshot 2024-12-09 184650.png>)

![alt text](<images/Screenshot 2024-12-09 184106.png>)

- Access the Application:
- Open the browser with the  IP address.

![alt text](<images/Screenshot 2024-12-09 184121.png>)



## Why Use GKE?
- ` High Availability: Ensures application uptime even during node failures.`
- ` Scalability: Automatically adjusts resources based on traffic and usage.`
- `Managed Kubernetes: Google handles the control plane and master nodes, simplifying operations.`

## Cost Optimization Strategies
- `Enable Cluster Autoscaler to optimize the number of nodes.`
- `Use preemptible VMs for non-critical workloads.`
- `Choose smaller machine types (e.g., e2-medium) when possible.`
- `Regularly audit and delete unused resources.`

### Future Enhancements

- Use a CI/CD pipeline for automated deployments using GCP services like Cloud Build, Cloud Deploy, and Artifact Registry.



