
# app/main.py

from fastapi import FastAPI
from app.api import user_routes
from app.core.config import settings
from app.core.logger import setup_logger
from app.models.user import Base
from app.db.session import engine
from app.services.file_services import router as services_router


# Create database tables
Base.metadata.create_all(bind=engine)

# initialize logger
logger = setup_logger()

# create FastAPI app
app = FastAPI(title=settings.APP_NAME)

# register routes
app.include_router(user_routes.router)
app.include_router(services_router)


@app.get("/")
def root():
    """
    Health check endpoint
    """
    logger.info("Root endpoint accessed")

    return {"message": "Backend Modular_API_SERVICES Running"}

