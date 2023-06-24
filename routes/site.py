from fastapi import APIRouter, Response, HTTPException
from config.db import client
from schemas.site import siteEntity, sitesEntity
from models.site import Site
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_201_CREATED

site = APIRouter()


@site.get("/sites")
def find_all_sites(skip: int = 0, limit: int = 10):
    try:
        total_sites = client.local.site.count_documents({})
        sites = client.local.site.find().skip(skip).limit(limit)
        return {
            "data": sitesEntity(sites),
            "total_sites": total_sites,
            "skip": skip,
            "limit": limit,
            "next_skip": skip + limit,
        }
    except Exception as e:
        return {"error": str(e)}


@site.post("/sites")
def create_site(site: Site):
    try:
        new_site = dict(site)
        client.local.site.insert_one(new_site).inserted_id
        return Response(status_code=HTTP_201_CREATED, content="Site created!")
    except Exception as e:
        return {"error": str(e)}


@site.get("/sites/{id}")
def find_site(id: str):
    try:
        site = client.local.site.find_one({"_id": ObjectId(id)})
        if site:
            return siteEntity(site)
        else:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND, detail="Site not found!"
            )
    except Exception as e:
        return {"error": str(e)}


@site.put("/sites/{id}")
def update_site(id: str, site: Site):
    try:
        updated_site = client.local.site.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": dict(site)}, return_document=True
        )
        if updated_site:
            return {"data": siteEntity(updated_site), "message": "Site updated!"}
        else:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND, detail="Site not found!"
            )
    except Exception as e:
        return {"error": str(e)}


@site.delete("/sites/{id}")
def delete_site(id: str):
    try:
        deleted_site = client.local.site.find_one_and_delete({"_id": ObjectId(id)})
        if deleted_site:
            return Response(status_code=HTTP_204_NO_CONTENT, content="Site deleted!")
        else:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND, detail="Site not found!"
            )
    except Exception as e:
        return {"error": str(e)}
