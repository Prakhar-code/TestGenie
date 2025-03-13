# TestGenie Backend

This repository contains the backend for the VS Code Extension **TestGenie**. The backend is built using **FastAPI**, a modern, fast (high-performance), web framework for building APIs with Python 3.7+.

## Features

- Provides API endpoints for the TestGenie extension.
- Handles test generation and management.
- Integrates seamlessly with the VS Code extension.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the server)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Prakhar-code/TestGenie.git
    cd TestGenie-backend
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

Start the FastAPI server using Uvicorn:
```bash
uvicorn app.run:app --reload
```

The server will be running at `http://127.0.0.1:8000`.

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- `http://127.0.0.1:8000/docs` (Swagger UI)
- `http://127.0.0.1:8000/redoc` (ReDoc)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

# Author

Prakhar Kabra

[LinkedIn](https://www.linkedin.com/in/prakhar-kabra-98a2521ba/) 

