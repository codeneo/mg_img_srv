# Multi Group Image Serve

## Overview

A restful backend web service written in Django to share images publicly via image groups/collection.

## Installation

In a Python3 environment, preferably a virtual one, execute the following in terminal or command prompt to install the dependencies:

```
pip install -r requirements.txt
```

## Project setup

The database is pre filled, as follows, to test out api's rapidly.

- **Users:**
 - admin : admin
 - first\_user : first\_user
 - second\_user : second\_user

- **Image Groups:**
 - First Image Group, owned by and associated with first\_user
 - Second Image Group, owned by and associated with first\_user
 - Third Image Group, owned by first\_user and associated with second\_user
 - Fourth Image Group, owned by and associated with second\_user
 - Fifth Image Group, owned by and associated with second\_user

- **Photos:**
 - Photos 1 through 30, owned by first\_user and present in First Image Group.
 - Photos 31 through 60, owned by first\_user and present in Second Image Group.
 - Photos 61 through 75, owned by first\_user and present in Third Image Group.
 - Photos 76 through 90, owned by second\_user and present in Third Image Group.
 - Photos 91 through 120, owned by second\_user and present in Fourth Image Group.
 - Photos 121 through 150, owned by second\_user and present in Fifth Image Group.

There are 150 photos with 30 photos from each category in cat, dolphin, panda, pigeon and sunflower randomly spread across the five image groups. Each category is part of the tag attribute of the photos. Almost all the other attributes are empty or have some default values.

## Run the project

From the project directory execute the following in terminal or a command prompt. Henceforth, login via the admin user at `localhost:8000/admin` to view the databases.

```
python manage.py runserver
```

## API Endpoints

- /api/v1/**account**/
- /api/v1/**register**/
- /api/v1/**login**/ 
- /api/v1/**logout**/
- /api/v1/**groups**/
- /api/v1/**groups**/{group-id}
- /api/v1/**photos**/
- /api/v1/**photos**/{photo-id}
- /api/v1/**photos**/?group={group-id}

Except **register** and **login** api's, all the other api's work in authenticated mode with token authentication mechanism provided by Django Rest Framework. The token is sent in this header, `'Authorization: Token <token>'`. **Groups** and **photos** endpoints are paginated with page size as 10.

## Improvements

- A more granular implementation of viewsets and serializers.
- JWT token which supports expiration

## Image Dataset

The images used in this project is a subset of the Caltech101 image dataset found at http://www.vision.caltech.edu/Image_Datasets/Caltech101/.