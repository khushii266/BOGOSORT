import http.server
import socketserver

PORT = 8000

class GodotServer(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # These headers are required for Godot 4 HTML5 exports to run locally
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

# Set up and run the server
with socketserver.TCPServer(("", PORT), GodotServer) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
