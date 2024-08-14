# capstoneproject2024

# Movie Listing API

## Overview

The Movie Listing API is a FastAPI-based application that allows users to list movies, view listed movies, rate them, and add comments. The application is secured using JWT (JSON Web Tokens), ensuring that only authorized users can perform certain actions like editing or deleting movies. The API also supports nested comments on movies.

## Features

- **User Authentication:**
  - User registration
  - User login with JWT token generation
  - Password hashing for security

- **Movie Listing:**
  - List a movie (authenticated users only)
  - View all movies (public access)
  - Edit a movie (only by the user who listed it)
  - Delete a movie (only by the user who listed it)

- **Movie Rating:**
  - Rate a movie (authenticated access)
  - Get ratings for a movie

- **Comments:**
  - Add a comment to a movie (authenticated access)
  - View comments for a movie (authenticated access)
  - Add nested comments to a comment (public access)

## Technology Stack

- **Backend Framework:** FastAPI (Python)
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)
- **Logging:** Python's built-in logging module
- **Testing:** Pytest
- **Deployment:** AWS (or any cloud provider)

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- `pip` (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/movie-listing-api.git
   cd movie-listing-api
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database:**

   Create a PostgreSQL database and configure the connection settings in the `.env` file:

   ```text
   DATABASE_URL=postgresql://username:password@localhost/dbname
   ```

5. **Run database migrations:**

   Use Alembic or another migration tool to set up the database schema:

   ```bash
   alembic upgrade head
   ```

6. **Start the application:**

   Run the FastAPI server using Uvicorn:

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be accessible at `http://127.0.0.1:8000`.

### API Documentation

FastAPI provides an automatic interactive API documentation that can be accessed at:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

### Testing

Run the tests using Pytest:

```bash
pytest
```

### Logging

Logs are written to `app.log` by default. The logging configuration can be customized in the `main.py` file.

### Deployment

To deploy the application on a cloud server like AWS, follow these general steps:

1. **Set up an EC2 instance** with your preferred OS.
2. **Install dependencies** on the server (Python, PostgreSQL, etc.).
3. **Transfer your code** to the server.
4. **Configure environment variables** on the server.
5. **Run Uvicorn** using a process manager like `systemd` or `supervisord`.
6. **Set up a reverse proxy** using Nginx or Apache to forward traffic to Uvicorn.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- FastAPI Documentation: https://fastapi.tiangolo.com/
- PostgreSQL Documentation: https://www.postgresql.org/docs/
- JWT Documentation: https://jwt.io/

---
