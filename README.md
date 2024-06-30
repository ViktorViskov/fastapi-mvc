<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>

# FastAPI MVC

This template provides a starting point for building web applications using FastAPI and following the Model-View-Controller (MVC) architectural pattern.

## Technologies Used

This project is developed using the following technologies:

- **FastAPI:** A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Uvicorn:** A lightning-fast ASGI server, used to run FastAPI application.
- **PyMySQL:** A pure-Python MySQL/MariaDB client library.
- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Alembic:** A database migration tool for SQLAlchemy.

## Project Structure

The project structure is organized as follows:

- **controllers:** Contains the controllers responsible for handling requests and business logic.
- **db:** Contains the database driver and logic for create database and working with tables.
- **middlewares:** Houses various middleware for request handling (e.g., static files, CORS).
- **models:** Stores the application's data models and schemas.
- **services:** Implements business logic for working with objects.
- **static:** Contaim static files (Some js library, css, images, etc.).
- **templates:** Holds HTML templates for rendering views.
- **utils:** Contains utility functions.

```
├── app
│   ├── constants.py
│   ├── controllers
│   │   ├── auth_controller.py
│   │   ├── page_controller.py
│   │   └── user_controller.py
│   ├── db
│   │   ├── context.py
│   │   └── user_db.py
│   ├── db_init.bash
│   ├── db_init.py
│   ├── dev.bash
│   ├── main.py
│   ├── middlewares
│   │   ├── cors_middleware.py
│   │   └── static_middleware.py
│   ├── models
│   │   ├── db.py
│   │   ├── dto.py
│   ├── prod.sh
│   ├── services
│   │   ├── jwt_service.py
│   │   └── user_service.py
│   ├── static
│   ├── templates
│   │   └── main.jinja
│   └── utils
│       ├── background_schedule_task.py
│       ├── bcrypt_hashing.py
│       ├── dependencies.py
│       ├── formating.py
│       ├── lifespan.py
│       └── sha256_hashing.py
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
    cd fastapi_mvc
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
