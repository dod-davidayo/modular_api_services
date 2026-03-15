from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Central Configuration Class.

    loads environment variable automatically.
    """

    APP_NAME: str
    DEBUG: bool
    DATABASE_URL: str

    class config:
        env_file = ".env"


# Create Global Settings instance
settings =  Settings()