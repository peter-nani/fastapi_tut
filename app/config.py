import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
ENV = os.getenv("ENV", "development")

# Other config like CORS origins, secrets can go here
