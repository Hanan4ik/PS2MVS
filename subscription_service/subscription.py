import requests as r
import base64 as b
from http.server import BaseHTTPRequestHandler, HTTPServer

# TODO server inbounds
# server1_inb = url_yeow
# server_2_inb = url2_yeow
#...
#servern_inb = urln_yeow

sub = b.b64encode("\n".join(...).encode('utf-8'))


host_name = "localhost" # TODO sys.argv
port = 8080 # TODO sys.argv

class SubService(BaseHTTPRequestHandler):
    def GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("profile-title", "TODO: config name")
        desc = b.b64encode("TODO config description".encode("utf-8")).decode("utf-8")
        self.send_header("announce", f"base64:{desc}")
        self.end_headers()
        self.wfile.write(sub)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), SubService)
    print(f"Server started http://{host_name}:{port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
