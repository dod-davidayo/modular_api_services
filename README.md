# AI-Assisted Development & Prompt Engineering
These projects were developed using AI-assisted engineering techniques. I applied prompt engineering strategies to collaborate with ChatGPT in order to design, architect, and implement the backend systems.

The goal was not to generate code blindly, but to use AI as a technical co-pilot to accelerate development while maintaining strong backend engineering practices.

# How Prompt Engineering Was Used

During development, structured prompts were used to guide the AI in producing production-ready backend patterns. Prompts focused on specific backend engineering tasks such as:

1) Designing scalable folder architectures

2) Implementing configuration management

3) Creating API endpoints

4) Structuring service layers

5) Handling file uploads and storage patterns

6) Applying dependency injection patterns

Example prompt used during development:

Design a production-ready Python backend template using FastAPI
that includes modular folder architecture, configuration management,
logging, dependency injection, and service-layer based architecture.

The AI-generated suggestions were then: Reviewed, Refactored, Integrated into the project architecture, This workflow helped accelerate development while maintaining clean code standards and maintainable architecture.

# Python Backend Engineering Projects

This repository contains backend engineering projects built to develop strong expertise in **backend architecture, scalable API design, and production-ready Python services**.

The projects focus on building clean, maintainable backend systems using modern Python backend technologies.

---

# Projects Overview

## 1. Modular API Service (Backend Template)

A production-style backend template designed for building scalable backend systems.

This project demonstrates how to structure a professional backend application with proper separation of concerns.

### Features

- Modular project architecture
- Environment configuration management
- Centralized logging system
- Dependency injection
- Database session management
- Service layer for business logic
- API routing structure
- Error handling patterns

### Folder Structure
Modular_API_SERVICES/
├── app/
│ ├── api/
│ ├── core/
│ ├── db/
│ ├── models/
│ ├── schemas/
│ ├── service/
│ └── services/
  |___ storage/
│
├ 
├── requirements.txt
├── .env
└── README.md

### Key Concepts Learned

- Scalable backend architecture
- Clean code principles
- Dependency injection
- Configuration management
- API design best practices

---

# 2. File Storage Service

A backend service designed to handle file uploads and file management operations.

This project demonstrates backend patterns for **document ingestion systems**, which are commonly used in AI platforms and data processing systems.

### Features

- File upload API
- File metadata management
- File retrieval
- File deletion
- Streaming file upload support
- Handling large file uploads

### API Endpoints

POST /upload  
Upload a file to the storage system

GET /files  
Retrieve a list of stored files

GET /files/{id}  
Retrieve information about a specific file

DELETE /files/{id}  
Delete a stored file


### Key Concepts Learned

- File streaming
- Asynchronous API development
- Storage architecture patterns
- Handling large file uploads
- Backend service design

---

# Technologies Used

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Loguru
- Uvicorn

---

# Installation

Clone the repository:


git clone https://github.com/dod-davidayo/modular_api_services.git 


Navigate into the project:


cd python-backend-engineering


Create a virtual environment:


python -m venv venv


Activate the environment:

Windows


venv\Scripts\activate


Mac/Linux


source venv/bin/activate


Install dependencies:


pip install -r requirements.txt


---

# Running the Server

Start the backend server using:


uvicorn app.main:app --reload


Open API documentation:


http://127.0.0.1:8000/docs


This will open the interactive API documentation powered by FastAPI.

---

# Future Improvements

Planned improvements include:

- JWT authentication
- Docker containerization
- Redis caching
- Background task processing
- Cloud storage integration (S3)
- API rate limiting

---

# Learning Objectives

These projects were built to develop strong skills in:

- Backend architecture
- Scalable API development
- Production-ready Python services
- Clean code and maintainable systems

---

# Author

David Durojaiye  
AI Backend Engineer