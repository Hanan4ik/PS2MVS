from requests import get, post
from helpers import server_link, get_random, client_param, dictify_by_domain, dictify_first
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
        self.totalGB = client_param("totalGB")

    def dictify(self):
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
        to_return = '{"clients": [{' \
        f'\n "id": "{self.id}",' \
        f'\n "flow": "{self.flow}",' \
        f'\n "email": "{self.email}",' \
        f'\n "limitIp": {self.limitIp},' \
        f'\n "totalGB": {self.totalGB},' \
        f'\n "expiryTime": {self.expiryTime},' \
        f'\n "enable": true,' \
        f'\n "tgId": "{self.tgId}",' \
        f'\n "subId": "{self.subId}",' \
        f'\n "comment": "{self.comment}",' \
        f'\n "reset": {self.reset}\n' \
        '}]}'
        self.email = get_random(8)
        return to_return

# TODO with writed cookie in main
def get_inbound_list(server: dict, cookie: dict):

    link = server_link(server)
    response = get(f"{link}/panel/api/inbounds/list", headers={"Accept": "application/json"}, cookies=cookie)
    response_json = response.json()
    response.close()
    return response_json['obj']

def get_inbound_list_ids(server: dict, cookie: dict):

    inbounds = get_inbound_list(server, cookie)
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

# TODO Trojan, vmess, shadowsocks, hysteria. And others later
def new_client(server:dict, cookie:dict, client:Client):
    for i in get_inbound_list_ids(server, cookie):
        payload={'id': i, 'settings': client.jsonify()}
        response = post(f"{server_link(server)}/panel/api/inbounds/addClient", data=payload, headers={"Accept": "application/json"}, cookies=cookie)


if __name__ == "__main__":
    serv = dictify_by_domain('nefor.site')
    new_client(serv, cookie(serv), Client(1053108667, 'Test'))
    get_inbound_list(serv, cookie(serv))
