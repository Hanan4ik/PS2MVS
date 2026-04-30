from requests import get
from helpers import server_link

def get_inbound_list(server: dict):

    link = server_link(server)

    response = get(f"{link}/panel/api/inbounds/list", headers={"Accept": "application/json"})
    response_json = response.json()
    print(response_json)
    response.close()

if __name__ == "__main__":
    get_inbound_list(server)
