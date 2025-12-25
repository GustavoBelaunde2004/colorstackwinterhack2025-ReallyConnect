"""
Supabase database client singleton.

This module provides a shared Supabase client instance that all services
can import and use. The client uses the service role key to bypass RLS
and perform administrative operations.
"""
import sys
from pathlib import Path
from supabase import create_client, Client

# Add backend directory to Python path for config import
backend_dir = Path(__file__).parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from config import settings

# Create Supabase client singleton
supabase: Client = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SERVICE_ROLE_KEY
)

