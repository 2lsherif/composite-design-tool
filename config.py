from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from the .env file

FLASK_ENV = os.getenv("FLASK_ENV")
DATABASE_URL = os.getenv("DATABASE_URL")
