from requests import get, post
from helpers import server_link, dictify_by_domain, dictify_first
from login import cookie
import json

# TODO with writed cookie in main
def get_inbound_list(server: dict, cookie: dict):

    link = server_link(server)
    response = get(f"{link}/panel/api/inbounds/list", headers={"Accept": "application/json"}, cookies=cookie)
    response_json = response.json()
    response.close()
    return response_json['obj']


def get_inbound(server: dict, inbound_id: int, cookie: dict):

    link = server_link(server)
    
    response = get(f"{link}/panel/api/inbounds/get/{inbound_id}", headers={"Accept": "application/json"}, cookies=cookie)
    response_json = response.json()
    response.close()
    return response_json['obj']

def get_client_by_tg(tgId):
    clients = json.loads(get_inbound(dictify_first(), 1, cookie(dictify_first()))["settings"])["clients"]
    for client in clients:
        if client["tgId"] == tgId:
            return client
    return None

def new_client(tgId):
    pass

if __name__ == "__main__":
   
    print(get_client_by_tg(1053108666))

