from fastapi import HTTPException

def raise_exception(status, message: str) -> Exception:
    raise HTTPException(
        detail = message, 
        status_code = status
    )