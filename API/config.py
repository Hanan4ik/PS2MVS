from os.path import exists
from os import mkdir
from helpers import dictify_all, client_param, server_link
from requests import get as GET

def check_config():
    if not exists("config"): mkdir("config")
 

def check_client_config() -> bool:
    check_config()
    if not exists("config/client.conf"):
        return False
    if client_param("limitIp") is None:
        return False
    if client_param("totalGB") is None:
        return False
    if client_param("reset") is None:
        return False

    return True



def generate_client_config(force: bool = False) -> None:

    if check_client_config(): return

    with open("config/client.conf", "w") as f:
        print("Let's create client.conf file")
        if input("Do you wish to continue [Y/n]").lower() not in "y ":
            return

        limitIp = input("Enter limit of IPs (0 for unlimited): ")
        totalGB = input("Enter maximum traffic in GB (0 for unlimited): ")
        reset = input("Enter how frequently traffic should be reset (0 for no reset): ")
        f.write(f"limitIp={limitIp}\ntotalGB={totalGB}\nreset={reset}")

def check_server_config() -> bool:
    check_config()
    if not exists("config/server_list.conf"):
        return False
    for server in dictify_all():    
        if GET(server_link(server)).status_code != 200:
            return False

    return True
    

# TODO inline server assignment
# TODO adding new servers
def generate_servers_config(force: bool = False) -> None:
    
    if check_server_config() and not force:
        return
    
    with open("config/server_list.conf", "w") as f:


        f.write("""# HERE'S THE TEMPLATE FOR ASSIGNING VPN-SERVER RUNNING 3X-UI
#
# <proto>://<username>:<password>@<hostname>:<port>/<secret_path>/
#
# EXAMPLE: https://coolname:s3Cr$t@example.com:443/UltRAM3g4SUpaSecretYeow/\n""")


        print("Can't find server_list.conf. Let's create it from scratch")
        cnt = 0
        while input("Do you wish to continue? [Y/n] ").lower() != "n":
            proto = input("Enter protocol of accessing panel (http/https): ")
            domain = input("Enter ip/domain of server: ")
            port = input("Enter panel access port: ")
            path = input("Enter path(endpoint) to access panel: ")
            if path.startswith("/") and path != "/": path = path[1:]
            username = input("Enter panel username: ")
            password = input("Enter panel password: ")
            link = f"{proto}://{username}:{password}@{domain}:{port}/{path}"
            f.write(link + "\n")
            print("Added server")
            cnt += 1
        if not cnt:
            print("No server added. Lookup config/server_list.conf to assign later")
        else:
            print(f"Added {cnt} server{"s" if cnt != 1 else ""}")

# Assumes that server list already assigned
def generate_subscription_config(force: bool = False) -> None:
    if not exists("config"): mkdir("config")
    if exists("config/subscription.conf") and not force:
        print("Subscription service already configured")
        return
    
    print("Can't find subscription.conf. Let's create it from scratch")
    if input("Do you wish to continue? [Y/n] ").lower() == "n":
        return
    with open("config/subscription.conf", "w") as f:
        title = input("Enter subscription title: ")
        desc = input("Enter subscription description: ")
        #sub -> domain:port/sub_path
        for server in dictify_all():
            print("Set subscription url for", server["domain"])
            port = input("Enter subscription port for", server['domain']+": ")
            sub_path = input("Enter subscription secret path for," server['domain']+": ")
            f.write(f"{server['proto']}://{server['domain']}:{port}/{sub_path}/") # append sub_id of client






