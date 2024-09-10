from fastapi import FastAPI
from sqlalchemy import create_engine

app = FastAPI()

# Define the MySQL connection URL
DATABASE_URL = "mysql+pymysql://user:password@db:3306/mydatabase"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

@app.get("/")   
def read_root():
    return {"message": "Hello world!"}
