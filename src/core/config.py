from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Dimburo"
    VERSION: str = "0.1.0"
    DATABASE_URL: str = "sqlite:///./test.db"

    @property
    def DEBUG(self) -> bool:
        return self.ENVIRONMENT == "dev"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()