"""
Script to start both backend and frontend servers for the algorithmic trading platform
"""
import subprocess
import sys
import os
import threading
import time
import webbrowser
import socket

def run_backend():
    """Function to run the backend server"""
    backend_dir = os.path.join(os.path.dirname(__file__), "backend")
    os.chdir(backend_dir)
    
    print("Installing backend dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    
    print("Starting backend server on http://localhost:8000")
    subprocess.run([sys.executable, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"])

def run_frontend():
    """Function to run the frontend server"""
    frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
    os.chdir(frontend_dir)
    
    # Check if npm is available
    try:
        subprocess.run(["npm", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Installing frontend dependencies...")
        subprocess.run(["npm", "install"], check=True)
        
        print("Starting frontend server on http://localhost:3000")
        subprocess.run(["npm", "run", "dev"])
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nNOTE: Node.js/npm is not installed or not in PATH")
        print("The frontend cannot be started automatically.")
        print("To run the frontend:")
        print("  1. Install Node.js from https://nodejs.org/")
        print("  2. Navigate to the frontend directory")
        print("  3. Run 'npm install' to install dependencies")
        print("  4. Run 'npm run dev' to start the frontend")
        print("\nThe backend is running on http://localhost:8000")
        
        # Automatically open the browser to the backend API documentation
        print("Opening browser to backend API documentation at http://localhost:8000/docs")
        webbrowser.open('http://localhost:8000/docs')

def main():
    """Main function to start both servers"""
    print("Starting Algorithmic Trading Platform...")
    print("This will start both the backend (port 8000) and frontend (port 3000)")
    
    # Start backend in a separate thread
    backend_thread = threading.Thread(target=run_backend)
    backend_thread.daemon = True
    backend_thread.start()
    
    # Give backend a moment to start
    time.sleep(3)
    
    # Start frontend in the main thread
    run_frontend()

if __name__ == "__main__":
    main()