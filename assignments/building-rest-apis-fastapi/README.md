# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that handles a list of items through GET, POST, and detail endpoints. This assignment introduces routing, request models, and basic API responses.

## 📝 Tasks

### 🛠️ Create Your First FastAPI App

#### Description
Set up a minimal FastAPI application and create a home endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance.
- Add a `GET /` route that returns a JSON message such as `{"message": "Welcome to the FastAPI assignment"}`.
- Run the app locally and confirm the root endpoint responds.

### 🛠️ Build Item Endpoints

#### Description
Add endpoints to create and read items from an in-memory list.

#### Requirements
Completed program should:

- Create a `GET /items` endpoint that returns all stored items.
- Create a `POST /items` endpoint that accepts item data and stores it.
- Return the created item as JSON after a successful POST request.

### 🛠️ Add Validation with Pydantic

#### Description
Use a Pydantic model to validate incoming item data.

#### Requirements
Completed program should:

- Define an `Item` model with fields such as `name`, `description`, and `price`.
- Ensure invalid requests are rejected with useful validation errors.
- Use the model in the POST endpoint so new items are created with consistent structure.
