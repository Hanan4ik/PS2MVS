from requests import post
from helpers import server_link
def get_auth_cookie(server_list: list[dict]):
    
    for server in server_list:
        response = post(f"{server_link(server)}/login", data={"username":server["username"], "password":server["password"]})
        server["auth_cookie"] = "".join(response.cookies.values())
        response.close()

if __name__ == "__main__":
    from consts.SERVERS import SERVERS
    get_auth_cookie(SERVERS)
    print(SERVERS[0]["auth_cookie"])

