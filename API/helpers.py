from os.path import exists
from os import mkdir


# JUST TO MAKE CODE A BIT READABLE

def get_config() -> str:
    with open("config/server_list.conf") as f:
        result = ""
        for line in f:
            line = line.replace(" ", "")
            if "#" in line:
                line = line[:line.find("#")]
            if not line:
                continue
            result += line + "\n"
    return result[:-1]



def dictify_all() -> list:
    servers = get_config()
    ar = []
    for server in servers.split():
        i = server.find("://")
        proto = server[:i]
        server = server[i+3:]

        i = server.find(":")
        username = server[:i]
        server = server[i+1:]

        i = server.find("@")
        password = server[:i]
        server = server[i+1:]

        i = server.find(":")
        domain = server[:i]
        server = server[i+1:]

        i = server.find("/")
        port = server[:i]
        server = server[i+1:]

        path = server
        ar.append({
                "proto": proto,
                "username": username,
                "password": password,
                "domain": domain,
                "port": port,
                'path': path
            })
    return ar

def dictify_first():
    server = get_config().split()[0]
    i = server.find("://")
    proto = server[:i]
    server = server[i+3:]

    i = server.find(":")
    username = server[:i]
    server = server[i+1:]

    i = server.find("@")
    password = server[:i]
    server = server[i+1:]

    i = server.find(":")
    domain = server[:i]
    server = server[i+1:]

    i = server.find("/")
    port = server[:i]
    server = server[i+1:]
            
    path = server
    return {
        "proto": proto,
        "username": username,
        "password": password,
        "domain": domain,
        "port": port,
        "path": path
    }

   

def dictify_by_domain(domain: str) -> dict:
    servers = get_config()
    # <proto>://<us>:<pswd>@<dmn>:<port>/<path>
    for server in servers.split():
        if f"@{domain}:" in server:
            i = server.find("://")
            proto = server[:i]
            server = server[i+3:]

            i = server.find(":")
            username = server[:i]
            server = server[i+1:]

            i = server.find("@")
            password = server[:i]
            server = server[i+1:]

            i = server.find(":")
            domain = server[:i]
            server = server[i+1:]

            i = server.find("/")
            port = server[:i]
            server = server[i+1:]
            
            path = server
            return {
                "proto": proto,
                "username": username,
                "password": password,
                "domain": domain,
                "port": port,
                "path": path
            }

def server_link(server: dict) -> str:
    return f"https://{server['domain']}:{server["port"]}/{server["path"]}"

# SETTING UP SERVERS

# TODO
def is_right_link(link: str) -> None:
    pass

# TODO inline server assignment
# TODO adding new servers
def generate_servers_config(force: bool = False) -> None:
    if not exists("config"): mkdir("config")
    if exists("config/server_list.conf") and not force:
        print("Servers already assigned")
        return

    with open("config/server_list.conf", "w") as f:
            

        f.write("""# HERE'S THE TEMPLATE FOR ASSIGNING VPN-SERVER RUNNING 3X-UI
#
# <proto>://<username>:<password>@<hostname>:<port>/<secret_path>/
#
# EXAMPLE: https://coolname:s3Cr$t@example.com:443/UltRAM3g4SUpaSecretYeow/\n""")


        print("Can't find server_list.conf. Let's create it from scratch")
        cnt = 0
        while input("Do you wish to continue? [Y/n]").lower() != "n":
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

def generate_client_config(force: bool = False) -> None:
    if not exists("config"): mkdir("config")
    if exists("config/client.conf") and not force:
        print("Client config already present")
        return
    with open("config/client.conf", "w") as f:
        pass
        #TODO
        

# INBOUND HELPERS

def client_param(param: str):
    with open("config/client.conf") as config:
        for p in config:
            p = p.split()
            if p[0] == param:
                return p[1]
    return None

if __name__ == "__main__":
    print(dictify_all())
