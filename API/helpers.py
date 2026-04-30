from os.path import exists
# JUST TO MAKE CODE A BIT READABLE

def server_link(server: dict) -> str:
    return f"https://{server['domain']}:{server["panel_port"]}/{server["secret_path"]}"

# SETTING UP SERVERS

# TODO
def is_right_link(link: str) -> None:
    pass

# TODO inline server assignment
# TODO adding new servers
def generate_servers() -> None:

    if not exists("config/server_list.conf"):
        with open("config/server_list.conf", "w") as f:
            

            f.write("""// HERE'S THE TEMPLATE FOR ASSIGNING VPN-SERVER RUNNING 3X-UI
//
// <proto>://<username>:<password>@<hostname>:<port>/<secret_path>/
//
// EXAMPLE: https://coolname:s3Cr$t@example.com:443/UltRAM3g4SUpaSecretYeow/\n""")


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
    servers = []
    with open("config/server_list.conf") as f:
        print("Found server_list.conf")
        for line in f:
            line = line.replace(" ", "")
            if "//" in line:
                line[line.find("//"):]
            if not line:
                continue
            i = line.find("://")
            proto = line[:i]
            line = line[i+3]

            i = line.find(":")
            username = line[:i]
            line = line[i+1:]

            i = line.find("@")
            password = line[:i]
            line = line[i+1:]

            i = line.find(":")
            domain = line[:i]
            line = line[i+1:]

            i = line.find("/")
            port = line[:i]
            line = line[i+1]

            path = line[1:]

            print(proto, username, password, domain, port, path)

if __name__ == "__main__":
    generate_servers()
