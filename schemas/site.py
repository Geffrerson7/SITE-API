def siteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "code": item["code"],
        "name": item["name"],
        "subproject": item["subproject"],
        "sector": item["sector"],
        "latitude": item["latitude"],
        "longitude": item["longitude"],
        "region": item["region"],
        "province": item["province"],
        "district": item["district"],
        "site_address": item["site_address"],
    }


def sitesEntity(entity) -> list:
    return [siteEntity(item) for item in entity]
