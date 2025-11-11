#!/usr/bin/env python3
"""
Simple local HTTP server for testing the theme system
This bypasses localStorage restrictions when using file:// protocol
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = "."

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add CORS headers to allow cross-origin requests if needed
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"\n🚀 Local server started!")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"🌐 Server URL: http://localhost:{PORT}/")
        print(f"\n📋 Available pages:")
        print(f"   • Home: http://localhost:{PORT}/index.html")
        print(f"   • Clock: http://localhost:{PORT}/clock.html")
        print(f"   • Theme: http://localhost:{PORT}/theme.html")
        print(f"\n💡 The theme system should now work properly!")
        print("   (localStorage is enabled with HTTP protocol)")
        print("\n⏹️  Press Ctrl+C to stop the server\n")
        
        # Open the main page in browser
        webbrowser.open(f"http://localhost:{PORT}/index.html")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

if __name__ == "__main__":
    start_server()