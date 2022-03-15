"""
Comic Maker Helper Script

In one command this script:
  - Sets up the venv
  - Runs the tool
  - Runs the test server.
"""

from pathlib import Path
import os, http.server, socketserver, platform

def setup_venv():
    print("Checking environment...")
    if Path("venv").exists(): 
        print("Found existing venv")
        return
    
    print("Setting up new venv...")

    if "Windows" in platform.system():
        os.system("python -m venv venv")
        os.system(".\\venv\\Scripts\\pip install -r requirements.txt")
    else:
        os.system("python3 -m venv ./venv")
        os.system("./venv/bin/pip install -r requirements.txt")

def run_server(outdir="dest"):
    os.chdir(outdir)

    print("Starting preview website on http://localhost:8000")
    print("Note this website will be slower than a real one.")
    print("Press Ctrl+C to exit.")

    Handler = http.server.SimpleHTTPRequestHandler

    class ReuseAddrServer(socketserver.TCPServer):
        allow_reuse_address = True
    

    httpd = ReuseAddrServer(("", 8000), Handler)
    try:
        with httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
        httpd.shutdown()
    

def run_comic_maker():

    print()
    print("Running the comic maker.")
    print("Please place your images in the comic_pages folder,")
    print("and press enter when ready!")
    input()

    if "Windows" in platform.system():
        os.system("venv\\Scripts\\python comicmaker.py")
    else:
        os.system("./venv/bin/python comicmaker.py")

    print()
    print("Your website files are now available in the dest folder.")
    print()


if __name__ == '__main__':
    setup_venv()
    run_comic_maker()
    run_server()