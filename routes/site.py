from fastapi import APIRouter

site = APIRouter()


@site.get("/sites")
def get_sites():
    return "Telecommunications sites!"
