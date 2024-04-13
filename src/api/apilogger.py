from fastapi import Request
from src.helper import apilog

async def apilogger(request: Request, call_next):
    data = {"url": request.url.path,
            "method": request.method,
            "query": request.query_params,
            "path": request.path_params
            }

    apilog.debug(data)

    response = await call_next(request)
    return response
