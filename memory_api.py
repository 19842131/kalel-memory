import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
from pathlib import Path

MEMORY_FILE = Path("/home/kali/kalel/sandbox/deepseek_chat_memory_v1/memory.md")
API_TOKEN = "KALEL_SECRET_2026"

class MemoryHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Permet de LIRE la mémoire via l'URL
        if self.path == "/memory.md" or self.path == "/":
            try:
                content = MEMORY_FILE.read_text()
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        # Permet d'ÉCRIRE dans la mémoire
        if self.path != "/save_memory":
            self.send_response(404); self.end_headers(); return
        
        auth = self.headers.get("Authorization")
        if auth != f"Bearer {API_TOKEN}":
            self.send_response(401); self.end_headers(); return

        length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(length))
        
        text = data.get("text", "")
        if text:
            with MEMORY_FILE.open("a") as f:
                f.write(f"\n\n### Sync {datetime.now().strftime('%Y-%m-%d %H:%M')}\n{text}\n")
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "success"}')
        else:
            self.send_response(400); self.end_headers()

if __name__ == "__main__":
    print("API Mémoire (Lecture+Écriture) sur le port 8081...")
    HTTPServer(('0.0.0.0', 8081), MemoryHandler).serve_forever()
