from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import platform
import os
import time
os_name = platform.system()

# Open port in firewall
if os_name == "Windows":
    os.system('netsh advfirewall firewall add rule name="Open Port 8000" dir=in action=allow protocol=TCP localport=8000')
elif os_name == "Linux":
    os.system("ufw allow 8000/tcp")

# Custom handler
class SilentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Ignore favicon
        
        if self.path.startswith("/favicon.ico"):
            self.send_response(204)
            self.end_headers()
            return

        # Parse query
        query_components = parse_qs(urlparse(self.path).query)
        msg = query_components.get("msg", [""])[0]

        # Save message silently
        if msg:
            with open("ai_face_persona/messages.txt", "w") as f:
                f.write(f"{time.time()}\n{msg}")

        # Send OK response
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    # Suppress default logging
    def log_message(self, format, *args):
        return

# Start server
server = HTTPServer(("0.0.0.0", 8000), SilentHandler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()

    # Remove firewall rules
    if os_name == "Windows":
        os.system('netsh advfirewall firewall delete rule name="Open Port 8000" protocol=TCP localport=8000')
    elif os_name == "Linux":
        os.system("ufw delete allow 8000/tcp")
