# Containerized Flask CRUD Learning Project with PostgreSQL

This repository contains a simple Flask application that demonstrates basic CRUD (Create, Read, Update, Delete) operations using a PostgreSQL database. The application and database are containerized using Docker and orchestrated with Docker Compose, making it easy to set up and run in any environment.

## Features
- **Flask Web Framework**: Utilizes Flask for building the web application.
- **PostgreSQL Database**: Uses a PostgreSQL database to store user data.
- **Docker Containerization**: Packages the Flask application and PostgreSQL database into separate Docker containers for easy deployment and scaling.
- **Docker Compose**: Simplifies the setup process by using Docker Compose to manage and orchestrate the multi-container application.
- **Environment Configuration**: Supports environment variable configuration for database connection settings.

## Structure
- **`docker-compose.yml`**: Defines two services: the Flask application and the PostgreSQL database, including environment variables, port mappings, and volume mounts for data persistence.
- **`app.py`**: The main application file containing the Flask app and route definitions.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-crud-learning.git
   cd flask-crud-learning
   ```
2. Ensure Docker and Docker Compose are installed on your machine.
3. Run the following command to build the Docker images and start the containerized application and database:
    ```bash
    docker-compose up --build
    ```
4. Access the Flask application at http://localhost:4002.

## API Endpoints
You can use the following endpoints to interact with the application:
- GET `/test`: A test route to check if the application is running.
- POST `/user`: Create a new user. (Request body should be JSON with username and email fields)
- GET `/users`: Retrieve all users.
- GET `/users/<id>`: Retrieve a user by ID.
- PUT `/users/<id>`: Update a user by ID. (Request body should be JSON with updated username and email fields)
- DELETE `/users/<id>`: Delete a user by ID.

