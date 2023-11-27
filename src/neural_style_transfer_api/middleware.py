from fastapi.middleware.cors import CORSMiddleware

## CORS ##
# Allow calling from different "origins"


def add_cors(app):
    origins = [
        "*",
        "http://localhost",
        "https://localhost",
        "http://localhost:8000",
        "https://localhost:8000",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )