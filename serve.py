#!/usr/bin/env python3
"""
Simple HTTP Server for Matrix AR Testing
=========================================

This script starts a local web server to test the Matrix AR experience.

Usage:
    python3 serve.py

The server will start on http://localhost:8000
Access the AR experience at: http://localhost:8000/matrix-ar.html

For testing on mobile devices:
1. Find your computer's IP address:
   - Mac/Linux: ifconfig | grep inet
   - Windows: ipconfig
   
2. On your phone (connected to same WiFi), navigate to:
   http://YOUR-IP-ADDRESS:8000/matrix-ar.html

Note: Modern browsers require HTTPS for camera access. If you encounter 
camera permission issues, use ngrok or GitHub Pages instead.
"""

import http.server
import socketserver
import os
import sys

# Configuration
PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to add CORS headers and better logging"""
    
    def end_headers(self):
        # Add CORS headers to allow cross-origin requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        # Cache control for development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Custom logging format with colors
        print(f"[{self.log_date_time_string()}] {format % args}")

def get_local_ip():
    """Try to get the local IP address"""
    import socket
    try:
        # Create a socket to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "Unable to determine"

def main():
    """Start the HTTP server"""
    
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create server
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            local_ip = get_local_ip()
            
            print("\n" + "="*70)
            print("🚀 MATRIX AR - LOCAL SERVER STARTED")
            print("="*70)
            print(f"\n✓ Server running on port {PORT}")
            print(f"\n📱 ACCESS OPTIONS:\n")
            print(f"   Local (this computer):")
            print(f"   → http://localhost:{PORT}/matrix-ar.html")
            print(f"   → http://127.0.0.1:{PORT}/matrix-ar.html\n")
            
            if local_ip != "Unable to determine":
                print(f"   Mobile/Tablet (same WiFi network):")
                print(f"   → http://{local_ip}:{PORT}/matrix-ar.html\n")
                print(f"   ⚠️  Note: Camera access may require HTTPS")
                print(f"   💡 If camera doesn't work, use ngrok or GitHub Pages\n")
            
            print("="*70)
            print("Press Ctrl+C to stop the server")
            print("="*70 + "\n")
            
            # Serve forever
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n" + "="*70)
        print("🛑 Server stopped by user")
        print("="*70 + "\n")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48 or e.errno == 98:  # Address already in use
            print("\n" + "="*70)
            print(f"❌ ERROR: Port {PORT} is already in use")
            print("="*70)
            print(f"\nTry one of these solutions:")
            print(f"1. Stop the process using port {PORT}")
            print(f"2. Use a different port (edit PORT variable in this script)")
            print(f"3. Wait a moment and try again\n")
            sys.exit(1)
        else:
            print(f"\n❌ ERROR: {e}\n")
            sys.exit(1)

if __name__ == "__main__":
    main()
