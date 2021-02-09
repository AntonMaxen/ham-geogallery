<center><h1>Ham Geo-Gallery</h1></center>
<!-- TABLE OF CONTENTS -->

<!--ts-->
## Table of Contents ##
* [Background](#background)
* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Roadmap](#roadmap)
  * [Planning](#planning-todo)
  * [Project](#project-todo)
* [Made by](#made-by)
<!--te-->

## Background ##


<!-- ABOUT THE PROJECT -->
## About The Project


### Built With
* [sqlalchemy](https://www.sqlalchemy.org/)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)


<!-- GETTING STARTED -->
## Getting Started

Follow the [installation](#installation) to get started

### Prerequisites

* Python 3+
* Docker
* Docker-compose

### Installation

1. Clone the repo
```sh
git clone https://github.com/AntonMaxen/webapp-project-pgbpyh20.git
```
2. Install requirements
```sh
pip install requirements.txt 
```
3. start docker containers
```sh
docker-compose up
```
4. run alembic upgrade
```
alembic upgrade head
```
5. run setup_databases file in app
6. Done

## Roadmap

### Planning TODO
 - [ ] Deadline is February 8th
 - [x] Choose database manager
 - [x] Chose Migration tool
 - [x] Plan UI
 - [x] Define naming conventions for database (plural/singular)
 - [x] Define functionality
 - [x] Make UML diagrams
 - [x] Setup project structure on github
 
 
 ### Project TODO
 - [x] Define how to use Googlemaps api (library/framework)
 - [x] Database Modeling + Figure out how cascading will work (delete comments on a review that is deleted)
 - [x] Define db naming conventions
 - [x] (Fixa docker)
 - [x] Setup Alembic Migrations
 - [x] Create SQLAlchemy Models
 - [x] Make Cascading work
 - [x] Create DB Repository (Figure out how the querys should work, what info do we want to get/add)
 - [x] Create Business Layer
 - [x] Create Flask Application
 - [x] Create UI Layer
 - [x] Integrate visual map (google maps api)
 - [x] UI Layer styling
 - [ ] Make unit test
 - [ ] Finsih Readme


## Made by
Anton Maxén, Henrik Liman, Mattias Barth
