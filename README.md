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

```
.
├── controllers/                # Handles route logic
│   ├── api/                    # API routes
│   └── pages/                  # Page-rendering controllers for frontend views
├── core/                       # Core application configuration and lifecycle
│   ├── middlewares/            # Custom middlewares
│   └── security/               # Security and auth logic
├── db_init.py                  # Script to initialize database schema
├── exceptions/                 # Custom exception handling
├── infrastructure/             # External services/integration layers
├── main.py                     # Application entry point
├── mappers/                    # Transforms between models and DTOs
├── migration_manager.sh        # Helper script for Alembic migrations
├── migrations/                 # Alembic migration folder
├── models/                     # Data schemas and enums
├── repos/                      # Data access layer (repositories)
├── schedulers/                 # Background task runners
├── services/                   # Business logic layer
├── static/                     # Static files (CSS, JS, images)
├── templates/                  # HTML templates rendered via Jinja2
├── utils/                      # Helper functions and shared utilities
└── views/                      # Rendered page views logic
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
