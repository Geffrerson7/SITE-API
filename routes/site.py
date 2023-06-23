from fastapi import APIRouter

site = APIRouter()


@site.get("/sites")
def find_all_sites():
    return "All sites!"

@site.post("/sites")
def create_site():
    return "Site created!"

@site.get("/sites/{id}")
def find_site():
    return "One site!"

@site.put("/sites/{id}")
def update_site():
    return "Site updated!"

@site.delete("/sites/{id}")
def delete_site():
    return "Site deleted!"