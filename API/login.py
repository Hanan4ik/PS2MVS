from requests import post
from helpers import server_link, dictify_by_domain
def cookie(server: dict):
    response = post(f"{server_link(server)}/login", data={"username":server["username"], "password":server["password"]})
    return {"3x-ui": "".join(response.cookies.values())}



if __name__ == "__main__":
    print(cookie(dictify_by_domain('nefor.site')))

