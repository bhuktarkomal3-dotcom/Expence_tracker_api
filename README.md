# Expense Tracker API

A REST API built with Python and FastAPI to manage personal expenses. Users can create an account, log in, add expenses, view their spending, update records, and delete expenses.

**Live API:** https://expence-tracker-api-xrdc.onrender.com

**API Docs:** https://expence-tracker-api-xrdc.onrender.com/docs

## Features

- User registration and login
- JWT-based authentication
- Add, view, update, and delete expenses
- Filter expenses by category and date range
- Get monthly expense summaries
- Store user and expense data in PostgreSQL
- SQLite support for local development
- Docker support

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL / SQLite
- JWT Authentication
- Docker
- Git and GitHub

## Run Locally

Clone the repository:

```bash
git clone https://github.com/bhuktarkomal3-dotcom/Expence_tracker_api.git
cd Expence_tracker_api
```

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///./expenses.db
```

Use your own secret key. Keep `.env` private and never commit it to GitHub.

Start the server:

```bash
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs to try the API.

## Main Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/auth/register` | Register a user |
| POST | `/auth/login` | Log in and get an access token |
| POST | `/expenses/` | Add an expense |
| GET | `/expenses/` | View expenses |
| GET | `/expenses/{expense_id}` | View one expense |
| PUT | `/expenses/{expense_id}` | Update an expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |
| GET | `/expenses/summary/monthly` | Get monthly spending total |

Expense endpoints require authentication.

## Run with Docker

Build the image:

```bash
docker build -t expense-tracker-api .
```

Run the container:

```bash
docker run --rm -p 8000:8000 --env-file .env expense-tracker-api
```

Then open http://127.0.0.1:8000/docs.

## What I Learned

While building this project, I worked with FastAPI routes, database models, password hashing, JWT authentication, CRUD operations, environment variables, Docker, and deployment on Render.

## Future Improvements

- Add automated tests
- Add expense charts and spending insights
- Improve input validation and error handling
