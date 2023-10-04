
# SKELETON API FASTAPI

Este projeto é utilizado como estrutura básica para criação de serviços web.




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

## Reference

 - [FastAPI Documentation](https://fastapi.tiangolo.com/)
 - [testdriven.io](https://testdriven.io/courses/tdd-fastapi/)
 - [pytest](https://docs.pytest.org/en/6.2.x/contents.html)
 - [Flake8](https://flake8.pycqa.org/en/latest/)
 - [Clean Arch](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
 
## Author

- [@weslei.souza](weslei.souza@under.com.br)




