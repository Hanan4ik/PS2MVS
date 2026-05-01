from requests import get, post
from helpers import server_link, client_config, dictify_by_domain, dictify_first
from login import cookie
from misc import get_uuid
import json
import time

class Client:
    def __init__(self, tgId, comment=''):
        self.tgId = tgId
        self.id = get_uuid()
        self.email = get_random(8)
        self.subId = get_random(16)
        self.limitIp = client_param("limitIp")
        self.expiryTime = 1000*(time.time() + 2592000) # add date+1month
        self.flow = "" # TODO
        self.comment = comment
        self.reset = client_param("reset")

    def __init__(self, tgId, uuid, email, subid, expiryTime, comment):
        self.tgId = tgId
        self.id = uuid
        self.email = email
        self.subId = subId
        self.comment = comment
        self.flow = "" # TODO
        self.limitIp = client_param("limitIp")
        self.totalGB = client_param("totalGB")
        self.expiryTime = expiryTime
        self.reset = client_param("reset")

    def __dictify(self):
        return {
            "id": self.id,
            "flow": self.flow,
            "email": self.email,
            "limitIp": self.limitIp,
            "totalGB": self.totalGB,
            "expiryTime": self.expiryTime,
            "enabled": True,
            "tgId": self.tgId,
            "subId": self.subId,
            "comment": self.comment,
            "reset": self.reset
        }

    def jsonify(self):
        return json.dumps(self.__dictify(), ensure_ascii=False)

# TODO with writed cookie in main
def get_inbound_list(server: dict, cookie: dict):

    link = server_link(server)
    response = get(f"{link}/panel/api/inbounds/list", headers={"Accept": "application/json"}, cookies=cookie)
    response_json = response.json()
    response.close()
    return response_json['obj']

def get_inbound_list_ids(server: dict, cookie: dict):

    inbounds = get_inbound_list()
    return [i["id"] for i in inbounds]

# Inbound base
def get_inbound(server: dict, inbound_id: int, cookie: dict):

    link = server_link(server)
    
    response = get(f"{link}/panel/api/inbounds/get/{inbound_id}", headers={"Accept": "application/json"}, cookies=cookie)
    response_json = response.json()
    response.close()
    return response_json['obj']

# Inbound child. Client base
def get_clients_by_inbound(server: dict, inbound_id, cookie) -> dict:
    return json.loads(get_inbound(server, inbound_id, cookie)["settings"]["clients"])

# Inbound child. Client child
def get_client_by_uuid(server:dict, inbound_id, cookie: dict, uuid: str) -> dict:
    clients = get_clients_by_inbound(server, inbound_id, cookie)
    for client in clients:
        if client["id"] == uuid:
            return client
    return None

def get_client_by_tg(server:dict, inbound_id, cookie:dict, tgId):
    clients = get_clients_by_inbound(server, inbound_id, cookie)
    for client in clients:
        if client["tgId"] == tgId:
            return client
    return None

def new_client(server, tgId, cookie):
    client = Client(1053108667, "Максимка").jsonify()
    for i in get_inbound_list_ids(server, cookie):
        payload = {''}
        # TODO

if __name__ == "__main__":
    print(get_client_by_tg(1053108666))

