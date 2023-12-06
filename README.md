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

```
├── app
│   ├── controllers
│   │   ├── auth_controller.py
│   │   ├── base_controller.py
│   │   ├── __init__.py
│   │   ├── page_controller.py
│   │   └── user_controller.py
│   ├── db_init.py
│   ├── dev.bash
│   ├── middlewares
│   │   ├── auth_middleware.py
│   │   ├── cors_middleware.py
│   │   ├── __init__.py
│   │   └── static_middleware.py
│   ├── models
│   │   ├── db.py
│   │   ├── dto.py
│   │   ├── __init__.py
│   │   └── other.py
│   ├── prod.sh
│   ├── repositories
│   │   ├── base_repository.py
│   │   ├── __init__.py
│   │   ├── token_repository.py
│   │   └── user_repository.py
│   ├── routers
│   │   ├── api_router.py
│   │   ├── auth_router.py
│   │   ├── base_router.py
│   │   ├── error_page_router.py
│   │   ├── __init__.py
│   │   ├── private_pages_router.py
│   │   └── public_pages_router.py
│   ├── services
│   │   ├── base_service.py
│   │   ├── __init__.py
│   │   ├── token_service.py
│   │   └── user_service.py
│   ├── static
│   ├── templates
│   │   ├── 403.html
│   │   ├── 404.html
│   │   ├── forgot.html
│   │   ├── login.html
│   │   ├── main.html
│   │   ├── private.html
│   │   └── register.html
│   ├── utils
│   │   ├── formating.py
│   │   ├── hashing.py
│   │   └── __init__.py
│   └── web.py
├── .env
├── docker-compose.yml
├── Dockerfile
├── install_env.sh
├── LICENSE
├── README.md
└── requirements.txt
```

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
