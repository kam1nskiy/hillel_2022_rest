# Hillel REST API app

# Setup


## Mandatory steps
1. Install Python 3.9+
2. Install Pipenv

## Installation 

Install deps 
Setup environment
```bash 
# Create virtual env
pipenv sync
pipenv shell
```

Run Django Server
```bash 
# Run migrations only on a project
python manage.py migrate

# Run Server
python src/manage.py runserver 
```

## Formatters and Checkers

Using black code format tool
``` 
python -m black ./
```
Using flake8
``` 
flake8 ./
```

Using isort
```
isort ./
```