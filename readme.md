<center><h1>Ham Geo-Gallery</h1></center>
<img src= "https://github.com/AntonMaxen/ham-geogallery/blob/dev/_documents/ham.png">

## Background ##
We started this project as a schoolassignment to create a webapplication with a databaseconnection. In the planning process, we got inspired by a orienteering website where you check in to checkpoints via googlemaps. We took that idea with a spin-off where a user can upload their own places on the map and upload photos on that location. The geogallery was born.


<!-- ABOUT THE PROJECT -->
## About The Project ##
ham-geogallery is a flask-webapplication with a googlemaps integration, you can add places, reviews, images as a logged in user. Its a good way to explore the world via the integrated map-gallery.


### Built With ##
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
git clone https://github.com/AntonMaxen/ham-geogallery.git
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
5. run populate_database
6. start webapp

## Roadmap

### Planning TODO
 - [x] Deadline is February 8th
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
 - [x] Make unit test
 - [x] Finsih Readme


## Made by
Anton Maxén, Henrik Liman, Mattias Barth
