from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def exception_middleware(request: Request, call_next):
    """Exception middlware."""

    try:
        return await call_next(request)

    except ValueError as ex:
        return JSONResponse({
            'error': str(ex),
        }, status_code=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:
        return JSONResponse({
            'error': str(ex),
        }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
