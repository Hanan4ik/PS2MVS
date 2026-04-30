from requests import get
from helpers import server_link

def get_inbound(server: dict, inbound_id):

    link = server_link(server)
    
    response = get(f"{link}/panel/api/inbounds/get/{inbound_id}", headers={"Accept": "application/json"}, cookies={"3x-ui": server["auth_cookie"]})
    response_json = response.json()
    print(response_json)
    response.close()

if __name__ == "__main__":
    get_inbound(server, 1)
