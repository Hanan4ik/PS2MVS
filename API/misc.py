from requests import get
from helpers import dictify_first

def get_uuid():
    link = server_link(dictify_first())
    response = get(f"{link}/panel/api/inbounds/list", headers={"Accept": "application/json"}, cookies=cookie)
    uuid = response.json()['obj']
    response.close()
    return uuid


