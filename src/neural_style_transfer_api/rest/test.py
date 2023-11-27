from fastapi import APIRouter, Request
from fastapi.responses import Response

from pydantic import BaseModel
from typing import Optional, Callable, Tuple, Protocol, Dict, Any

router = APIRouter()

@router.get('/test')
def test_endpoint(request: Request):
    print(request)
    print(f"\n[DEBUG]: Context {request.scope['aws.context']}")
    return {
        "aws_event": request.scope["aws.event"],
        # "aws_context": request.scope["aws.context"],
        "scope": [str(x) for x in request.scope.keys()],
    }
