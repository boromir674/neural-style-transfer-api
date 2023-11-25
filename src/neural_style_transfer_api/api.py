from fastapi import FastAPI

from .realtime import (
    nst_websocket_router,
    ex_websocket_router
)
from .rest import nst_v1_router


app = FastAPI()


# ROUTE / WIRE Endpoints
app.include_router(nst_websocket_router)
app.include_router(ex_websocket_router)
app.include_router(nst_v1_router)
