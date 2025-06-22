# Containerized Search Engine App using FastAPI and Elasticsearch

![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?logo=elasticsearch&logoColor=white)
![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?logo=google-cloud&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)


The repository contains a containerized microservices architecture using Docker, comprising a frontend, backend, and Elasticsearch, all deployed on a cloud platform (GCP) and managed entirely via the command-line interface.


## 🔧 Key Features & Technical Highlights

- **Containerized Microservices:**  
  Each service in the three-tier architecture—frontend, backend, and Elasticsearch—is containerized using production-optimized Dockerfiles.  
  ➤ *Ensures environment consistency, simplifies deployment, and enhances portability across development and production.*

- **Multi-Tier Architecture:**  
  The application follows a modular, layered structure separating the UI (frontend), business logic (backend), and search/indexing (Elasticsearch).  
  ➤ *Improves maintainability, allows independent scaling of services, and enforces a clear separation of concerns.*

- **Docker Networking via Container Names:**  
  A custom Docker bridge network is configured, enabling containers to communicate with each other using **container names instead of IP addresses**.  
  ➤ *Provides DNS-based name resolution, increases reliability, and avoids issues with dynamic container IPs.*

- **Persistent Data Storage:**  
  Docker volumes are mounted for the Elasticsearch container to persist indexed data across container restarts and removals.  
  ➤ *Prevents data loss and ensures continued search functionality during updates or reboots.*

- **CLI-Driven Cloud Deployment (GCP):**  
  The entire system is deployed on **Google Cloud Platform (GCP)** using only the command-line interface (CLI), with no reliance on graphical tools.  
  ➤ *Demonstrates proficiency in headless server environments, automation, and cloud-native deployment.*

- **Docker Image Optimization:**  
  Each Dockerfile is crafted using multi-stage builds, minimal base images (e.g., Alpine), and secure runtime configurations.  
  ➤ *Reduces image size, improves container startup time, and minimizes security vulnerabilities.*


##  System Architecture
The diagram below illustrates the high-level architecture of the frontend, the backend, and the Elasticsearch database container across two virtual machines.



![Screenshot 2025-06-22 at 1 08 49 PM](https://github.com/user-attachments/assets/01c106b2-0aaf-45e8-82af-096f7a641a2b)



## Tech Stack

| Layer        | Technology                                   | Purpose                                                    |
|--------------|----------------------------------------------|------------------------------------------------------------|
|   Frontend  | HTML, CSS, JavaScript (served via FastAPI)   | Renders the user interface, delivered through the backend  |
|  Backend   | FastAPI (Python)                              | Handles API requests, application logic, and routing       |
|  Database  | Elasticsearch                                 | Enables powerful full-text search and data indexing        |
|  DevOps    | Docker, Docker Compose                        | Containerization and orchestration of microservices        |
|  Cloud     | Google Cloud Platform (GCP)                   | Cloud deployment and infrastructure hosting                |



## Repository Structure

```

├── backend/
│ └── app/
│ ├── Dockerfile
│ ├── main.py
│ └── requirements.txt
│
├── elasticsearch/
│ ├── docker-compose.yml
│ ├── elasticsearch/
│ └── setup/
│
├── frontend/
│ └── app/
│ ├── templates/
│ │ └── index.html
│ ├── Dockerfile
│ ├── main.py
│ └── requirements.txt
│
├── optimised/
│ ├── Dockerfile.backend
│ └── Dockerfile.frontend
```


