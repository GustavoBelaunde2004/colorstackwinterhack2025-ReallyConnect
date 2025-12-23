import os
from typing import Optional
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""
    
    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
    SUPABASE_JWT_SECRET: Optional[str] = os.getenv("SUPABASE_JWT_SECRET", None)
    
    def __init__(self):
        """Validate required settings on initialization."""
        self._validate_settings()
    
    def _validate_settings(self) -> None:
        """Ensure all required environment variables are set."""
        if not self.SUPABASE_URL:
            raise ValueError("SUPABASE_URL environment variable is required")
        if not self.SUPABASE_SERVICE_ROLE_KEY:
            raise ValueError("SUPABASE_SERVICE_ROLE_KEY environment variable is required")


# Global settings instance
settings = Settings()

