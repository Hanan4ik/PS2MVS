from os.path import exists
from os import mkdir

def generate_client_config(force: bool = False) -> None:
    if not exists("config"): mkdir("config")
    if exists("config/client.conf") and not force:
        print("Client config already present")
        return
    with open("config/client.conf", "w") as f:
        print("Let's create client.conf file")
        if input("Do you wish to continue [Y/n]").lower() not in "y ":
            return

        limitIp = input("Enter limit of IPs (0 for unlimited): ")
        totalGB = input("Enter maximum traffic in GB (0 for unlimited): ")
        reset = input("Enter how frequently traffic should be reset (0 for no reset): ")
        f.write(f"limitIp={limitIp}\ntotalGB={totalGB}\nreset={reset}")

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


def generate_subscription_config(force: bool = False) -> None:
    if not exists("config"): mkdir("config")
    if exists("config/subscription.conf") and not force:
        print("Subscription service already configured")
        return

    with open("config/server_list.conf", "w") as f:



