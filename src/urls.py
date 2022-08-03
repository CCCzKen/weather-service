from src.views import api, index


routers = (
    (index.bp, ''),
    (api.bp, '/api'),
)
