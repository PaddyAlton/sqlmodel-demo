# sqlmodel-demo
Experimenting with SQLModel/FastAPI

## About the application

I was interested in building something with non-trivial complexity in order to force myself to reason about things like relationships between SQL records (as described via SQLModel) and extend the examples in the documentation (as opposed to just copy/pasting them and changing some names).

To this end I created an API that allows end users to manage a database of data about church congregations. It's a nice example because we have a clear hierarchy of one-to-many relationships:

- parishioners belong to one parish, parishes have many parishioners
- parishes belong to one diocese, dioceses have many parishes 

SQLModel is used to interact with the SQL database and FastAPI is the framework used by the application.

## Trying it out

There are two supported ways to run the application.

### Docker

If you have Docker, then simply copy the example files in `sqlmodel-demo/config` in order to provide 
- `config/api.env`
- `config/db.env`

and then run 

> `docker-compose up`

You should get:

1. a postgres DB service `sqlmodel-demo-db`
2. an API service `sqmodel-demo-api`

The containers may be configured (for example, to use a secret password) by changing the `.env` files in `config/`.

These containers run on a shared Docker network, `demo-network`. The API is bound to and served on `localhost:8765` and the database has a mounted Docker volume, `church-db-data`, that provides data persistence.

`ctrl + C` is enough to bring the containers down, but `docker-compose down --volumes` is required for full clean-up.

### Pipenv

An alternative is to run the application in a virtual environment, courtesy of Pipenv. Note that Pipenv is being used to manage dependencies whichever way you run the application.

To start the application with Pipenv:

- run `pipenv install` to set up a virtual environment and install the dependencies
- create a top-level environment file `sqlmodel-demo/.env` using the template `sqlmodel-demo/.env.example`
- run `pipenv run start` to serve the application via `uvicorn`
- note that this will create a SQLite Database `sqlmodel-demo/test.db` if you haven't changed the connection string from that given in `.env.example`)
- make HTTP requests to the application (runs on `localhost:8765` by default)

## Interacting with the application

Once the application is running, you can view the auto-generated Swagger documentation at [http://localhost:8765/docs]().

Currently the API manages three resources:

- dioceses
- parishes
- parishioners

POST, GET, and DELETE are supported. For example, POST to `localhost:8765/diocese` will create a new diocese record. GET to `localhost:8765/diocese/<id>` will return the record, and DELETE to the same URI will delete the record from the database.

Endpoints likewise exist for `/parish` and `/parishioner`.
