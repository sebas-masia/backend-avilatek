# FastAPI E-Commerce API

## Overview

This project is a RESTful API for an e-commerce platform built using FastAPI. The API allows users to manage products and orders, including functionality for user authentication and authorization using JWT tokens. The project integrates with a PostgreSQL database for persistent data storage and is designed with scalability and maintainability in mind.

## Architecture

The project follows a modular architecture with the following key components:

- **FastAPI**: The main framework used to build the API.
- **PostgreSQL**: The relational database management system used to store data.
- **SQLAlchemy**: The ORM used to interact with the PostgreSQL database.
- **Alembic**: Used for database migrations.
- **Docker**: Used for containerization, making the application easy to deploy and scale.
- **JWT Authentication**: Secures the API endpoints by authenticating users with JSON Web Tokens (JWT).

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Python 3.12**: The programming language used for this project.
- **PostgreSQL**: The database system used for storing product and order data.
- **SQLAlchemy**: An ORM that provides a set of high-level APIs to interact with the database.
- **Alembic**: A database migration tool to handle schema changes.
- **Docker**: Containerization technology used to package the application and its dependencies.
- **Uvicorn**: ASGI server used to serve the FastAPI application.

## Features

- **User Registration and Authentication**: Securely register and authenticate users using JWT tokens.
- **Product Management**: Create, read, update, and delete products. Supports cascading deletes.
- **Order Management**: Users can create orders, and the system automatically updates product stock.
- **Database Migrations**: Automatically apply database migrations using Alembic.
- **Dockerized Setup**: Easily deploy the application using Docker.

## Running the Project

### Running with Docker

#### Prerequisites

- **Docker**: Make sure Docker is installed on your machine.
- **Docker Compose**: Docker Compose should be installed as well.

#### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Build and start the containers**:
   ```bash
   docker-compose up --build
   ```
3. **Access the API**:
   The FastAPI application should be running on http://localhost:8000
4. **Stopping the containers**
   ```bash
   docker-compose down
   ```

### Running locally without Docker

#### Prerequisites

- **Python 3.12**: Ensure Python is installed on your machine
- **PostgreSQL**: Install and set up PostgreSQL locally

#### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Set up your virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**
   - Create a PostgreSQL database and user
   - Update `DATABASE_URL` in `app/database.py` to match your local PostgreSQL configuration:
   ```python
   DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:admin@localhost:5432/db_store")
   ```
5. **Run alemebic migrations**
   Apply database migrations to set up the schema:
   ```bash
   alembic upgrade head
   ```
6. **Start the FastAPI application**:
   ```bash
   uvicorn main:app --reload
   ```
7. **Access the API**:
   The FastAPI application should be running on http://localhost:8000

## API Documentation

- FastAPI provides interactive API documentation out of the box. Once the application is running, you can access the
  SwaggerUI at: - http://localhost:8000/docs
- You can also access the alternative ReDoc documentation at:
  - http://localhost:8000/redoc
