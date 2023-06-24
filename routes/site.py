from fastapi import APIRouter
from config.db import client
from schemas.site import siteEntity, sitesEntity
from models.site import Site
from bson import ObjectId

site = APIRouter()


@site.get("/sites")
def find_all_sites():
    return sitesEntity(client.local.site.find())


@site.post("/sites")
def create_site(site: Site):
    new_site = dict(site)
    client.local.site.insert_one(new_site).inserted_id
    return "Site created!"


@site.get("/sites/{id}")
def find_site(id:str):
    return siteEntity(client.local.site.find_one({"_id": ObjectId(id)}))


@site.put("/sites/{id}")
def update_site():
    return "Site updated!"


@site.delete("/sites/{id}")
def delete_site():
    return "Site deleted!"
