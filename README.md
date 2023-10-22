
# SKELETON FASTAPI

---

# Python Boilerplate with FastAPI and Tortoise ORM

## Overview

Welcome to the repository of my Python Boilerplate with FastAPI, Tortoise ORM, and Aerich. This project was created with the idea of providing a modular and flexible structure, based on the principles of Domain-Driven Design (DDD) and Clean Architecture, but with a lighter, more 'pythonic' approach.

## Key Features

- **Pythonic Modularity:** The architecture of this boilerplate is designed with an emphasis on modularity, allowing for a more organized and easily extendable code structure.
- **FastAPI for Rapid Development:** Harness the power of FastAPI to quickly build robust and scalable APIs with minimal development effort.
- **Tortoise ORM and Aerich for Data Persistence:** Utilize Tortoise ORM to manage data persistence, ensuring efficient organization and simplified access to the application's data. Aerich is used to manage migrations smoothly and reliably.
- **Influences of DDD and Clean Architecture:** While adopting the concepts of DDD and Clean Architecture, we strive to maintain an approach more adapted to the Python ecosystem, keeping the code clean, readable, and easily maintainable.

## Getting Started

To get started, follow the installation and configuration instructions provided in the project's documentation section. Detailed documentation and practical examples will help you quickly understand how to make the most of this boilerplate.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


## Requirements


 - Python 3 
 - Pip
 - [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)


## How to work

### Clone this repository
`git clone git@bitbucket.org:undersoftware/skeleton-fastapi.git`

### Access project directory in terminal
`cd app_name`

### Install all dependencies
`pipenv install --dev`

### Enable environment
`pipenv shell`

### Make a copy dotenv file to environment file
`cp dotenv_example .env`

## If you prefer to use a database, use the commands below 
`make init_db` 
after 
`make migrate`

### Running application in development mode
`make run-app-local`

### The application is running in port:8000 - acesse <http://localhost:8000/health-check> 
## Running tests

For run tests, use this commands:

```bash
  pytest 
```
or
```bash
  make testing 
```

## For create new module, use this commands:
```bash
  make create_module 
```
## Contribution

Contributions are welcome! If you have any suggestions, issues, or wish to add new features, feel free to create a pull request. Please refer to the contribution guidelines in the CONTRIBUTING.md file.

I hope this boilerplate makes your work easier and helps drive your Python projects forward. Enjoy!

---
## Reference

 - [FastAPI Documentation](https://fastapi.tiangolo.com/)
 - [testdriven.io](https://testdriven.io/courses/tdd-fastapi/)
 - [pytest](https://docs.pytest.org/en/6.2.x/contents.html)
 - [Flake8](https://flake8.pycqa.org/en/latest/)
 - [Clean Arch](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
 
## Author

- [@weslei.souza](weslei.souza@under.com.br)




