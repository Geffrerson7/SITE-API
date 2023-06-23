def siteEntity(item)->dict:
    return {
        "id": item["id"],
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