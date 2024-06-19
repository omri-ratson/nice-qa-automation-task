# IMDB_api_backend_project

This repository contains a Django-based backend project that serves as a RESTful API for an IMDb-like application. It leverages the Django Rest Framework (DRF) to provide a range of API endpoints.

We recommend using IDE such as Jetbrains PyCharm or IntelliJ, but you could of course use VS Code to run this project or any other IDE of your choice.

# Installation
To run this project locally, follow these steps:

## 1. Clone the repository to your local machine using the following command:
```bash
git clone {this project}
```

## 2. Create a virtual environment to isolate the project dependencies:
```bash
python -m venv env
```
## 3. Activate the virtual environment:
```bash
.\env\Scripts\activate
```

## 4. Install the project dependencies:
```bash
pip install -r requirements.txt
```

## 5. Start the development server:
```bash
python manage.py runserver
```
The development server will be up and running at http://localhost:8000/ (you would see a page with 404 but that's fine).  
You can now access the API endpoints.

## 6. API Endpoints
The following API endpoints are available in this project:

### Movies
* `GET /watch/list`: Retrieve a list of all movies.
* `POST /watch/list`: Create a new movie.
* `GET /watch/list`/{id}: Retrieve details of a specific movie.
* `PUT /watch/list`/{id}: Update details of a specific movie.
* `DELETE /watch/list`/{id}: Delete a specific movie.
### Stream Platforms
* `GET /watch/stream`: Retrieve a list of all stream platforms.
* `POST /watch/stream`: add a new platform.
* `GET /watch/stream/{id}/`: Retrieve details of a specific streaming platform.
* `PUT /watch/stream{id}/`: Update details of a specific streaming platform.
* `DELETE /watch/stream/{id}/`: Delete a specific streaming platform.
### Reviews
* `GET /watch/stream/review/{id}/`: Retrieve review of a specific movie.
* `POST /watch/stream/{id}/review-create`: create a review for specific movie.

## 7. Swagger
Upon start of the application, a SwaggerUI can be accessed at - http://localhost:8000/swagger.  
This provides a user-friendly interface to interact with the API endpoints.

## 8. Tests
To run the integration tests for this project, use the following command:
```bash
python manage.py test watchlist_app.testsIntegration
```
<hr>
