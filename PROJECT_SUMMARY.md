# Flask Task API - Production Deployment on AWS

## Project Overview
A production-ready Flask REST API deployed on AWS with container orchestration, load balancing, auto-scaling, and monitoring.

**Live URL:** http://flask-app-alb-584296125.us-east-1.elb.amazonaws.com

**Deployment Date:** December 2025

---

## Architecture

### Final Production Architecture
```
Internet
   ↓
Application Load Balancer (port 80)
   ↓
ECS Fargate Service (auto-scaling 1-3 tasks)
   ↓
Docker Containers (Flask App)
```

### Components
- **Compute:** AWS ECS Fargate (serverless containers)
- **Load Balancing:** Application Load Balancer
- **Container Registry:** Amazon ECR
- **Monitoring:** CloudWatch (logs + metrics + dashboard)
- **Auto-scaling:** Target tracking based on CPU
- **Networking:** VPC with public subnets across multiple AZs

---

## API Endpoints

### Health Check
```bash
GET /health
Response: {"status": "healthy"}
```

### Get All Tasks
```bash
GET /tasks
Response: {"tasks": ["task1", "task2"]}
```

### Add Task
```bash
POST /tasks
Body: {"task": "your task"}
Response: {"message": "Task added", "task": "your task"}
```

### CPU Stress Test (for auto-scaling demo)
```bash
GET /stress
Response: {"message": "CPU stressed!", "result": 123456}
```

---

## Deployment Evolution

### Day 1: Dockerization
- Created Dockerfile
- Built container image locally
- Tested with Docker

### Day 2: EC2 Deployment
- Launched EC2 instance (t2.micro)
- Configured security groups
- Deployed Docker container manually
- Direct access via public IP

### Day 3: Load Balancer
- Created Application Load Balancer
- Set up target groups with health checks
- Routed traffic through ALB
- Blocked direct EC2 access

### Day 4: ECS Migration
- Pushed image to Amazon ECR
- Created ECS cluster (Fargate)
- Defined task and service
- Integrated with existing ALB
- Zero-downtime migration

### Day 5: Monitoring & Auto-scaling
- CloudWatch dashboard with CPU, memory, requests
- Auto-scaling policy (CPU target: 10%)
- Load tested with Apache Bench
- Verified scale-up (1 → 7 tasks) and scale-down (7 → 1 tasks)

---

## Technical Details

### Docker Image
- **Base:** python:3.12-slim
- **Size:** ~200MB
- **Registry:** 886989006163.dkr.ecr.us-east-1.amazonaws.com/flask-task-api

### ECS Configuration
- **Cluster:** flask-app-cluster
- **Service:** flask-app-service
- **Task Definition:** flask-app-task
- **Launch Type:** Fargate
- **CPU:** 0.5 vCPU
- **Memory:** 1 GB
- **Desired Tasks:** 1 (min: 1, max: 3)

### Auto-Scaling
- **Metric:** ECS Service Average CPU Utilization
- **Target:** 10%
- **Scale-out cooldown:** 60 seconds
- **Scale-in cooldown:** 60 seconds

### Security
- ALB Security Group: Allow HTTP (80) from anywhere
- ECS Security Group: Allow TCP (5000) only from ALB
- IAM roles for ECS task execution

---

## Load Testing Results

### Test Configuration
```bash
ab -n 10000 -c 200 -t 60 \
  http://flask-app-alb-584296125.us-east-1.elb.amazonaws.com/stress
```

### Results
- **Peak CPU:** 16.2%
- **Max tasks created:** 7 tasks
- **Scale-up time:** ~2 minutes
- **Scale-down time:** ~5 minutes
- **Zero dropped requests** during scaling events

---

## Key Learnings

### DevOps Concepts
- Containerization with Docker
- Infrastructure as Code principles
- Blue-green deployment capabilities
- Immutable infrastructure
- Observability and monitoring

### AWS Services
- **ECS:** Container orchestration
- **ECR:** Container registry
- **ALB:** Load balancing and health checks
- **CloudWatch:** Logging and metrics
- **VPC:** Networking and security
- **Auto Scaling:** Dynamic capacity management

### Best Practices Implemented
- ✅ Containerized application
- ✅ Load balancer for high availability
- ✅ Auto-scaling for cost optimization
- ✅ Health checks for reliability
- ✅ Centralized logging
- ✅ Security groups for network isolation
- ✅ Graceful shutdown (draining)
- ✅ Multi-AZ deployment

---

## Skills Demonstrated

### Technical Skills
- Docker containerization
- AWS cloud services (ECS, ECR, ALB, CloudWatch)
- Linux system administration
- Networking (VPC, subnets, security groups)
- Load balancing and auto-scaling
- CI/CD concepts (manual implementation)
- Monitoring and observability

### DevOps Practices
- Infrastructure management
- Deployment strategies
- Performance testing
- Troubleshooting and debugging
- Documentation

---

## Future Enhancements

### Next Steps (Week 3)
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Automated deployment on git push
- [ ] Environment variables management
- [ ] SSL/HTTPS with ACM certificate
- [ ] Custom domain name
- [ ] Database integration (RDS)
- [ ] Terraform for Infrastructure as Code

### Production Improvements
- [ ] Multi-region deployment
- [ ] CloudFront CDN
- [ ] WAF for security
- [ ] Secrets management with AWS Secrets Manager
- [ ] Cost optimization with Savings Plans
- [ ] Backup and disaster recovery

---

## Commands Reference

### Docker
```bash
# Build image
docker build -t flask-task-api .

# Run container locally
docker run -d -p 5000:5000 flask-task-api

# Push to ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin \
  886989006163.dkr.ecr.us-east-1.amazonaws.com

docker tag flask-task-api:latest \
  886989006163.dkr.ecr.us-east-1.amazonaws.com/flask-task-api:latest

docker push \
  886989006163.dkr.ecr.us-east-1.amazonaws.com/flask-task-api:latest
```

### Testing
```bash
# Health check
curl http://flask-app-alb-584296125.us-east-1.elb.amazonaws.com/health

# Load test
ab -n 10000 -c 200 \
  http://flask-app-alb-584296125.us-east-1.elb.amazonaws.com/stress
```

### AWS CLI
```bash
# View ECS service
aws ecs describe-services \
  --cluster flask-app-cluster \
  --services flask-app-service

# View tasks
aws ecs list-tasks \
  --cluster flask-app-cluster \
  --service-name flask-app-service

# View logs
aws logs tail /ecs/flask-app-task --follow
```

---

## Conclusion

Successfully deployed a production-ready containerized application on AWS with:
- High availability (multi-AZ)
- Automatic scaling (1-3 tasks)
- Comprehensive monitoring
- Load balancing
- Zero-downtime deployments

**Total project duration:** 5 days (Week 2)

**Skills gained:** Docker, AWS ECS/ECR/ALB, CloudWatch, Auto-scaling, Production deployment

---

## Author
**Phanindhra Sura**
- GitHub: https://github.com/Phanindhraaa
- Project: https://github.com/Phanindhraaa/flask-task-api

**Date:** December 2025
