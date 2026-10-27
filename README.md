# Expense Tracker API

A RESTful API built with Python and FastAPI to manage personal expenses with JWT-based authentication.

## Features

- User registration and login
- JWT-based authentication
- Create, view, update, and delete expenses
- Retrieve all expenses belonging to the authenticated user
- Filter expenses by category and date range
- Generate monthly spending summaries
- User-specific expense access and authorization
- Interactive API documentation with Swagger UI

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Authentication:** JWT
- **Testing interface:** Swagger UI

## Project Structure

```text
Expence_tracker_api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── users.py
│       └── expenses.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/bhuktarkomal3-dotcom/Expence_tracker_api.git
cd Expence_tracker_api
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the development server

```bash
python -m uvicorn app.main:app --reload
```

### 5. Open the API documentation

Visit:

http://127.0.0.1:8000/docs

Use Swagger UI to register, log in, authorize requests, and test the endpoints.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a user |
| POST | `/auth/login` | Log in and receive an access token |
| POST | `/expenses/` | Create an expense |
| GET | `/expenses/` | List and filter expenses |
| GET | `/expenses/{expense_id}` | Retrieve a specific expense |
| PUT | `/expenses/{expense_id}` | Update an expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |
| GET | `/expenses/summary/monthly` | Calculate monthly spending |

Expense endpoints require authentication. Users can access only their own expenses.

## Learning Outcomes

This project demonstrates REST API development, database integration, request validation, JWT authentication, and user-specific data access using FastAPI and SQLAlchemy.

## Project Status

Core API endpoints implemented and manually tested through Swagger UI. Automated tests and deployment are not yet implemented.

## Author

**Komal Bhuktar**

GitHub: [bhuktarkomal3-dotcom](https://github.com/bhuktarkomal3-dotcom)
