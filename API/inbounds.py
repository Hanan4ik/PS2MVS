from requests import get, post
from helpers import server_link, dictify_by_domain
from login import cookie
import json

# TODO with writed cookie in main
def get_inbound_list(server: dict):

    link = server_link(server)
    response = get(f"{link}/panel/api/inbounds/list", headers={"Accept": "application/json"}, cookies=cookie(server))
    response_json = response.json()
    response.close()
    return response_json['obj']
# TODO with writed cookie in main
def get_inbound(server: dict, inbound_id: int):

    link = server_link(server)
    
    response = get(f"{link}/panel/api/inbounds/get/{inbound_id}", headers={"Accept": "application/json"}, cookies=cookie(server))
    response_json = response.json()
    response.close()
    return response_json['obj']

if __name__ == "__main__":
    data = get_inbound(dictify_by_domain("nefor.site"), 1)
    print(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))
