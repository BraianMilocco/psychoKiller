# PsychoKiller

This Readme is in Work In Progress

# Table of Contents

- [Introduction](#introduction)
- [Backend](#backend)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Migrations](#migrations)
    - [Seeds](#seeds)
    - [Running](#running)
    - [Useful commands](#useful-commands)
      - [Autofromatter](#autofromatter)
      - [Linter](#linter)
- [Frontend](#frontend)
  - [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Running](#running)
- [Contributing](#contributing)
  - [Branches](#branches)
  - [Commits](#commits)
  - [PRs](#prs)
- [Docs](#docs)
  - [Model](#model)
- [Other](#other)

## Introduction

PsychoKiller is a tool that provides a way to manage and carry out psychology tests

It is developed as a web app using [Django](https://www.djangoproject.com/) as a backend framework and [React](https://reactjs.org/) to build the UI

## Backend

### Getting Started

#### Prerequisites

- [Python 3](https://www.python.org/)

- [Poetry](https://python-poetry.org/)

- DB to be defined

#### Setup

1. Go to Django folder, run: `cd back`

2. Install virtualenv `poetry install`

3. Optional: We have a recommended vscode setting file in `.vscode/recommended.settings.json`, we **strongy** suggest you to use that configuration, you only have to rename the file from `recommended.settings.json` to `settings.json`

4. Run migrations

#### Migrations

You should run these commands the first time you set up the repo and every time that you change the model

1. Create migrations: `poetry run python manage.py makemigrations psychoApp`

2. Run migrations: `poetry run python manage.py migrate`

3. Create a superuser to have access to the [Administrative Interface](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/) running `poetry run python manage.py createsuperuser` and follow instructions

4. Run seeds

#### Seeds

This provides actual data to the database once created. Seed data is located in `back/psychoApp/fixtures/` in JSON format
In order to load data you need to run `poetry run python manage.py loaddata --format json data_file_name`

**Important Note:** The order in which the seeds are run is important as once depends from the other because of relationships so you should load data in this order

1. Load template test data: `poetry run python manage.py loaddata --format json SCL90__template_test`

2. Load options data: `poetry run python manage.py loaddata --format json SCL90__options`

3. Load questions data: `poetry run python manage.py loaddata --format json SCL90__questions`

#### Running

1. Go to Django folder, run: `cd back`

2. To start the Django server run: `poetry run python manage.py runserver`

#### Useful commands

##### Autofromatter

We use `Black` as autoformatter

1. Go to Django folder, run: `cd back`

2. Run `poetry run black ./path-to-file` or `poetry run black ./` to run in every file in the project

##### Linter

1. Go to Django folder, run: `cd back`

1. Run `poetry run flake8 ./path-to-file` or `poetry run flake8 ./` to run in every file in the project

## Frontend

**_Skip this section for now - WIP_**

### Getting Started

#### Prerequisites

- [Node](https://nodejs.org)

- [NPM](https://www.npmjs.com/)

#### Setup

1. Run: `cd front/psycho_front`

2. Run: `yarn install`

#### Running

## Contributing

```
Como manejarse con Git:
    -En rama development se manejan los cambios, cada dev tendrá una rama de la cual trabajar, al iniciar
       la mergea con development, trabaja, una vez termina su trabajo pushea su rama, y cuando confirme que es código funcional se mergea a development
       Ej: git checkout mi_rama , git merge development (work) git add, git commit, git push mi_rama, git checkout development, git push development.

    -La rama main se va a actualizar mediante push request desde la rama development, ninguna otra rama se conecta con main.
```

### Branches

Please name your branches as follows `type_of_branch/developer_name/branch_description`

**type_of_branch possible values**

- `feature` - A feature branch
- `bugfix` - A bugfix branch
- `chore` - Changes to the build process or auxiliary tools and libraries
- `doc` - Documentation related changes
- `refactor` - A code change that neither fixes a bug nor adds a feature

### Commits

No conventions required when commiting to a branch as they will be squashed one PR is Merged, but for commmits done directly to the development branch the message should be like this:

```
type_of_commit: Main Message

Optional Description
```

`type_of_commit` possible values same as `type_of_branch`

### PRs

Please title PR as

`type_of_branch: Main Description`

Add optional Message to the body of the PR

Once approved please squash PR, title and message should follow same convention as PR.

## Docs

### Model

[Updated draw io Model](https://drive.google.com/file/d/10hqU88j-wviGUm4WkoZvQdNqPKNEO4dV/view?usp=sharing)

![Model](docs/ModeloDataBase_0_1.jpg)

## Other

```
Wip
```
