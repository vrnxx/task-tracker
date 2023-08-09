# Task-tracker

![Static Badge](https://img.shields.io/badge/fastapi-0.101.0-rgb(77%2C%20163%2C%20144))
![Static Badge](https://img.shields.io/badge/sqlalchemy-2.0-rgb(74%2C%2091%2C%20161))
![Static Badge](https://img.shields.io/badge/pydantic-2.1-rgb(176%2C%2035%2C%2073))
![Static Badge](https://img.shields.io/badge/alembic-1.11.1-green)




Simple service of FastAPI that implement patterns like a UoW, DAO, DTO ect.

<hr>

# Technologies
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Alembic

# Installation

- Clone this repository
```
  git clone git@github.com:AlexanderSeryakov/task-tracker.git
```
- Move to project directory
```
  cd task-tracker
```
- Install dependencies
```
  poetry install
```
> If poetry not installed on yor local machine, enter this command:
```
  pip install poetry
```
- Open terminal in project root and start database
```
  make up-db
```
- Start application
```
  make start-app
```