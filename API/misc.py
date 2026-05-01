from requests import get
from helpers import dictify_first, server_link
from login import cookie

def get_uuid():
    serv = dictify_first()
    link = server_link(serv)
    response = get(f"{link}/panel/api/server/getNewUUID", headers={"Accept": "application/json"}, cookies=cookie(serv))
    uuid = response.json()['obj']['uuid']
    response.close()
    return uuid


