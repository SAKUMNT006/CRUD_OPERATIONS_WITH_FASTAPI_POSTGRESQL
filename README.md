# FastAPI CRUD Operations with PostgreSQL

![image](https://github.com/SAKUMNT006/CRUD_OPERATIONS_WITH_FASTAPI_POSTGRESQL/assets/51531124/7ed1c29a-6d99-42aa-b4ad-1ca13f7d5a9f)

This is a simple demonstration of how to perform CRUD operations using the FastAPI framework and PostgreSQL as the database. It provides a RESTful API for managing resources and saving data to a PostgreSQL database.

## Prerequisites

Before running this project, ensure you have the following prerequisites installed:

- Python 3.7+
- Pip (Python package manager)
- PostgreSQL

## Installation

1. Create a virtual environment:

```
python3 -m venv venv
```

2. Activate the virtual environment:
```

On Windows:

```
venv\Scripts\activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Configuration

1. Update the PostgreSQL database connection details:

``` python
DATABASE_URL = "postgresql://username:password@localhost/database_name"
```

Replace `username`, `password`, and `database_name` with your own values.

## Database Setup

1. Create a PostgreSQL database with the name specified in the `DATABASE_URL` configuration.

## Usage

1. Start the FastAPI application:

```
uvicorn app.main:app --reload
```

2. Open your web browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to access the interactive API documentation (provided by Swagger UI).

3. You can now test the CRUD operations by making requests through the API endpoints.

## API Endpoints
## it is API Documentation created on swagger UI
### Create a Resource
```
{
    "openapi": "3.0.2",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items": {
            "get": {
                "summary": "Get All Items",
                "operationId": "get_all_items_items_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response Get All Items Items Get",
                                    "type": "array",
                                    "items": {}
                                }
                            }
                        }
                    }
                }
            }
        },
        "/item/{item_id}": {
            "get": {
                "summary": "Get An Item",
                "operationId": "get_an_item_item__item_id__get",
                "parameters": [
                    {
                        "required": true,
                        "schema": {
                            "title": "Item Id",
                            "type": "integer"
                        },
                        "name": "item_id",
                        "in": "path"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/items/post": {
            "post": {
                "summary": "Create An Item",
                "operationId": "create_an_item_items_post_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Item"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/item/put/{item_id}": {
            "put": {
                "summary": "Update An Item",
                "operationId": "update_an_item_item_put__item_id__put",
                "parameters": [
                    {
                        "required": true,
                        "schema": {
                            "title": "Item Id",
                            "type": "integer"
                        },
                        "name": "item_id",
                        "in": "path"
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Item"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/item/delete/{item_id}": {
            "delete": {
                "summary": "Delete Item",
                "operationId": "delete_item_item_delete__item_id__delete",
                "parameters": [
                    {
                        "required": true,
                        "schema": {
                            "title": "Item Id",
                            "type": "integer"
                        },
                        "name": "item_id",
                        "in": "path"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "HTTPValidationError": {
                "title": "HTTPValidationError",
                "type": "object",
                "properties": {
                    "detail": {
                        "title": "Detail",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/ValidationError"
                        }
                    }
                }
            },
            "Item": {
                "title": "Item",
                "required": [
                    "id",
                    "name",
                    "description",
                    "price",
                    "on_offer"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    },
                    "name": {
                        "title": "Name",
                        "type": "string"
                    },
                    "description": {
                        "title": "Description",
                        "type": "string"
                    },
                    "price": {
                        "title": "Price",
                        "type": "integer"
                    },
                    "on_offer": {
                        "title": "On Offer",
                        "type": "boolean"
                    }
                }
            },
            "ValidationError": {
                "title": "ValidationError",
                "required": [
                    "loc",
                    "msg",
                    "type"
                ],
                "type": "object",
                "properties": {
                    "loc": {
                        "title": "Location",
                        "type": "array",
                        "items": {
                            "anyOf": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "integer"
                                }
                            ]
                        }
                    },
                    "msg": {
                        "title": "Message",
                        "type": "string"
                    },
                    "type": {
                        "title": "Error Type",
                        "type": "string"
                    }
                }
            }
        }
    }
}
```


## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [python](https://www.python.org/)
  

