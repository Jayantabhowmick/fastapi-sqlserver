import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mssql+pyodbc://?odbc_connect=Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=fastapi_db;Trusted_Connection=yes;"
)

APP_NAME = "FastAPI SQL Server API"
APP_VERSION = "1.0.0"
DEBUG = os.getenv("DEBUG", "True") == "True"