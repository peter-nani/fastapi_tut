from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.api.v1 import users
from app.db import init_db

app = FastAPI(title="FastAPI Tut Example")

app.include_router(users.router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    # For dev convenience: create tables from models
    init_db()


def custom_openapi():
    # This function creates a custom OpenAPI schema that defines the structure of the API documentation.
    # The OpenAPI schema serves as a contract for the API, detailing the available endpoints, request/response formats, 
    # and other metadata. It is useful for generating interactive API documentation, client SDKs, and for ensuring 
    # consistency in API design.
    # Use cases for a custom OpenAPI schema include:
    # 1. Providing clear and interactive documentation for API consumers.
    # 2. Enabling automated generation of client libraries in various programming languages.
    # 3. Facilitating API testing and validation tools.
    # 4. Enhancing API discoverability and usability for developers.
    #     dict: The OpenAPI schema dictionary containing the API documentation structure.
    """
    Generate and customize the OpenAPI schema for the FastAPI application.
    
    This function creates a custom OpenAPI schema with a title and version.
    It caches the schema to avoid regenerating it on subsequent calls.
    
    The function performs the following steps:
    1. Checks if an OpenAPI schema is already cached in the app
    2. If cached, returns the existing schema immediately
    3. If not cached, generates a new OpenAPI schema using get_openapi() with:
       - Custom title: "FastAPI Tut Example"
       - Version: "1.0.0"
       - All application routes
    4. Stores the generated schema in app.openapi_schema for future use
    5. Returns the OpenAPI schema
    
    Returns:
        dict: The OpenAPI schema dictionary containing the API documentation structure
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(title="FastAPI Tut Example", version="1.0.0", routes=app.routes)
    # You can customize the schema here (add contact, license, etc.)
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
