from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from uuid import UUID
import sys
from pathlib import Path
import httpx
from config import settings

# BACKEND DIR FOR IMPORTING CONFIG
backend_dir = Path(__file__).parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))


security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> UUID:
    """
    FastAPI dependency to verify JWT token and extract user ID.
    
    Uses Supabase's User API endpoint to validate the token - this is the
    recommended approach for backend services as it doesn't require JWK endpoints
    and works with all Supabase auth methods (email, OAuth, etc.).
    
    Args:
        credentials: Bearer token from Authorization header
        
    Returns:
        UUID: The authenticated user's ID
        
    Raises:
        HTTPException: If token is invalid, expired, or missing
    """
    token = credentials.credentials
    
    try:
        # Verify token by calling Supabase's user endpoint
        # This validates the token and returns user info if valid
        user_url = f"{settings.SUPABASE_URL}/auth/v1/user"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                user_url,
                headers={
                    "Authorization": f"Bearer {token}",
                    "apikey": settings.SUPABASE_SERVICE_ROLE_KEY
                },
                timeout=5.0
            )
            
            if response.status_code == 401:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid or expired authentication token"
                )
            
            response.raise_for_status()
            user_data = response.json()
            
            # Extract user ID from response
            user_id_str = user_data.get("id")
            if not user_id_str:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token missing user ID claim"
                )
            
            # Convert to UUID
            try:
                user_id = UUID(user_id_str)
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid user ID format in token"
                )
            
            return user_id
            
    except HTTPException:
        raise
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token validation failed: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication error: {str(e)}"
        )
