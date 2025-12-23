from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from uuid import UUID
import sys
from pathlib import Path
from config import settings

# BACKEND DIR FOR IMPORTING CONFIG
backend_dir = Path(__file__).parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))


security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = security
) -> UUID:
    """
    FastAPI dependency to verify JWT token and extract user ID.
    
    Args:
        credentials: Bearer token from Authorization header
        
    Returns:
        UUID: The authenticated user's ID
        
    Raises:
        HTTPException: If token is invalid, expired, or missing
    """
    token = credentials.credentials
    jwt_secret = settings.SUPABASE_JWT_SECRET

    if not jwt_secret:
        # Note: In production, you should set SUPABASE_JWT_SECRET explicitly
        raise ValueError(
            "SUPABASE_JWT_SECRET must be set in environment variables. "
            "Get it from Supabase Dashboard > Settings > API > JWT Secret"
        )
    
    try:
        # Decode and verify JWT token
        payload = jwt.decode(
            token,
            jwt_secret,
            algorithms=["HS256"],
            options={"verify_signature": True, "verify_exp": True}
        )
        
        # Extract user ID from token claims
        user_id_str = payload.get("sub")
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
        
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication token: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication error: {str(e)}"
        )

