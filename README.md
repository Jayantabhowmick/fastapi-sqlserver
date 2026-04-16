# FastAPI + SQL Server API

A complete, production-ready Python API solution built with FastAPI and connected to SQL Server.

## 🚀 Features

- **FastAPI** - Modern, fast web framework for building APIs
- **SQL Server Integration** - SQLAlchemy ORM with SQL Server support
- **CRUD Operations** - Complete Create, Read, Update, Delete endpoints
- **Request Validation** - Pydantic models for data validation
- **Auto Documentation** - Automatic Swagger UI and ReDoc
- **Error Handling** - Proper HTTP exceptions and error responses
- **Connection Pooling** - Optimized database connections
- **Environment Configuration** - Secure .env configuration

## 📋 Prerequisites

- Python 3.8+
- SQL Server (local or remote)
- ODBC Driver 17 for SQL Server

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Jayantabhowmick/fastapi-sqlserver.git
cd fastapi-sqlserver
```

2. **Create virtual environment**
```bash
python -m venv venv

# Activate on Windows
venv\\Scripts\\activate

# Activate on macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your SQL Server credentials
```

## 🏃 Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

## 📚 API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 📊 Available Endpoints

### Users API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users/` | List all users |
| GET | `/api/users/{user_id}` | Get specific user |
| GET | `/api/users/active/users` | Get all active users |
| POST | `/api/users/` | Create new user |
| PUT | `/api/users/{user_id}` | Update user |
| DELETE | `/api/users/{user_id}` | Delete user |

## 📝 Example Usage

### Create a User
```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### Get All Users
```bash
curl http://localhost:8000/api/users/
```

### Update a User
```bash
curl -X PUT http://localhost:8000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Jane"
  }'
```

## 🗄️ Database Setup

The User table will be automatically created when the application starts. The table includes:

- `id` - Primary key
- `username` - Unique username
- `email` - Unique email address
- `first_name` - User's first name
- `last_name` - User's last name
- `is_active` - Account status
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

## 🔐 SQL Server Connection

Update your `.env` file with your SQL Server details:

```
DATABASE_URL=mssql+pyodbc://username:password@server:1433/database?driver=ODBC+Driver+17+for+SQL+Server
```

Or for Windows Authentication:
```
DATABASE_URL=mssql+pyodbc://?odbc_connect=Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=fastapi_db;Trusted_Connection=yes;
```

## 📁 Project Structure

```
fastapi-sqlserver/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration
│   ├── database.py          # Database setup
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # CRUD operations
│   └── routers/
│       ├── __init__.py
│       └── users.py         # User endpoints
├── requirements.txt         # Dependencies
├── .env.example            # Environment template
├── .gitignore              # Git ignore
└── README.md               # Documentation
```

## 🛠️ Development

To add new endpoints:

1. Create a model in `app/models.py`
2. Create schemas in `app/schemas.py`
3. Create CRUD operations in `app/crud.py`
4. Create router in `app/routers/`
5. Include router in `app/main.py`

## 🐛 Troubleshooting

### Connection Error
- Ensure SQL Server is running
- Verify connection string in `.env`
- Check ODBC driver is installed

### Import Errors
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt`

### Port Already in Use
```bash
uvicorn app.main:app --reload --port 8001
```

## 📝 License

This project is open source and available for educational and commercial use.

## 👨‍💻 Author

Created by Jayantabhowmick

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.
