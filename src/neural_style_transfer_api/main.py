from .api import app
from .middleware import add_cors


__all__ = ['app']

# Allow Cross-origin requests
add_cors(app)
