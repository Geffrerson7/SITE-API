from fastapi import FastAPI
from routes.site import site
from fastapi.openapi.utils import get_openapi

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Telecommunications Sites API",
        version="1.0.0",
        description="API to create telecommunications antennas sites",
        terms_of_service="https://policies.google.com/terms",
        contact={"name":"Gefferson Casasola", "email": "gefferson.casasola@gmail.com"},
        license_info={"name": "MIT License"},
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.include_router(site)
