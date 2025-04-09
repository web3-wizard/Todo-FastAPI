# Python FastAPI TODO App

A simple To-do application built with FastAPI to showcase the capabilities of the framework. This application serves as a starting point for building RESTful APIs with Python.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Fast and efficient API development
- Easy to use and understand
- Automatic interactive API documentation (Swagger UI and ReDoc)
- Asynchronous support for high performance

## Technologies

- [Python](https://www.python.org/) (3.7+)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3**: You can check if Python 3 is installed by running:
  
  ```bash
  python3 --version
  ```

- **Python 3 venv**: This package is required to create virtual environments. You can check if it's installed by running:

    ```bash
    python3 -m venv --help
    ```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/web3-wizard/Todo-FastAPI.git
   cd Todo-FastAPI
   ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, use the following command:

```bash
fastapi dev src/main.py
```

You can access the API at http://127.0.0.1:8000 and docs at http://127.0.0.1:8000/docs.

