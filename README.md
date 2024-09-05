# orp

## Introduction

The Open Regulation Platform (ORP) will provide a searchable and filterable list of UK regulations and legislation.

## Getting Started

The quickest way top get started is to use the `docker-compose` configuration
to run the application in a containerised environment.
Most of the actions required to run and manage the application are encapsulated
in the `Makefile`. First, in a working directory run:

    $ git clone git@github.com:uktrade/orp.git
    $ cd orp

The docker compose configuration requires that a `local.env` file is present.
An example file is provided in the repository. Create one like this:

    $ cp local.env.example local.env

This should work out of the box.

Prepare the application for first use:

    $ make first-use

Start the services:

    $ make start

> You may see [Sass deprecation warnings](https://frontend.design-system.service.gov.uk/installing-with-npm/#requirements), but these can be ignored.

Navigate a browser to:

    http://localhost:8081        # The serivce landing page

## Local development environment
While the `docker-compose` configuration is the quickest way to get started, it
can also be useful to create a development environment on your local machine.
However, your mileage may vary depending on your operating system. The following
instructions are for OSX.

### Prerequisites
As we are using python package `psycopg-c`, you need the PostgreSQL client
development headers (e.g. the `libpq-dev` package) installed on your system.
On Mac you can run the following command to install `libpq`:

    $ brew install libpq

> Note the dev files are included using this command.

### Requirements

- [`Python 3.12.*`](https://www.python.org/downloads/). Don't be tempted to use
  an earlier or later version of Python. Use Poetry to manage your Python version
  and dependencies.
- [`Docker Desktop`](https://docs.docker.com/get-docker/). A recent version
  (e.g. `4.30.0` or above) is recommended, which includes all the key components
  you'll require including `engine`, `build` and `compose`.

### Install Poetry
We use [Poetry](https://python-poetry.org/) to manage dependencies. Follow the
guidance in the [official documentation](https://python-poetry.org/docs/). On
OSX, run the following commands to install Poetry:

    $ brew install pipx
    $ pipx ensurepath
    $ pipx install poetry

Restart your terminal.

### Create a Poetry env and activate it

    $ poetry install
    $ poetry shell

### Installing pre-commit hooks

With your Poetry shell active:

    $ pre-commit install

> This will ensure that your code passes quality checks before you commit it.
> Code quality checks are also performed when pushing your code to origin
> but pre-commit hooks catch issues early and will improve Developer Experience.
