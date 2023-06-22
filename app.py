from fastapi import FastAPI
from routes.site import site

app = FastAPI()

app.include_router(site)
