# FastAPI MVC

This template provides a starting point for building web applications using FastAPI and following the Model-View-Controller (MVC) architectural pattern.

## Technologies Used

This project is developed using the following technologies:

- **FastAPI:** A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Uvicorn:** A lightning-fast ASGI server, used to run FastAPI application.
- **PyMySQL:** A pure-Python MySQL client library.
- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Alembic:** A database migration tool for SQLAlchemy.

## Project Structure

The project structure is organized as follows:

- **controllers:** Contains the controllers responsible for handling requests and business logic.
- **middlewares:** Houses various middleware for request handling (e.g., authentication, CORS).
- **models:** Stores the application's data models and schemas.
- **repositories:** Handles interaction with databases or external services.
- **routers:** Defines API routes and separates public/private access endpoints.
- **services:** Implements business logic and services.
- **templates:** Holds HTML templates for rendering views.
- **utils:** Contains utility functions.

## Getting Started

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ViktorViskov/fastapi-mvc.git
    ```

2. Install dependencies:

    ```bash
    cd fastapi_mvc_template
    pip install -r requirements.txt
    ```

### Running the Application

To start the FastAPI application, use the following command:

```bash
cd app
bash dev.bash
```

## Deploying the Project
```sh
docker compose up -d
```
