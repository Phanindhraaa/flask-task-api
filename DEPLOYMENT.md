# Deployment Notes

## Server Details
- Instance Type: t2.micro
- AMI: Ubuntu 24.04 LTS
- Public IP: 18.208.151.78
- Region: us-east-1 (or whatever you used)

## Deployed: December 24, 2025

## Access
- Health Check: http://18.208.151.78:5000/health
- API Endpoints: http://18.208.151.78:5000/tasks

## Container
- Image: flask-task-api
- Container name: flask-api
- Port: 5000

## Commands Used
```bash
docker build -t flask-task-api .
docker run -d -p 5000:5000 --name flask-api flask-task-api
docker ps
docker logs flask-api
```
