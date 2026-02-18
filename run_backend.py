"""
Script to run the algorithmic trading platform backend
"""
import subprocess
import sys
import os

def main():
    """Main function to start the backend server"""
    print("Starting Algorithmic Trading Platform Backend...")
    
    # Change to backend directory
    backend_dir = os.path.join(os.path.dirname(__file__), "backend")
    os.chdir(backend_dir)
    
    # Try to install simplified dependencies first
    print("Installing simplified dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "../requirements-simple.txt"], check=True)
        print("Simplified dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing simplified dependencies: {e}")
        print("Trying with original requirements...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "../requirements.txt"], check=True)
        except subprocess.CalledProcessError as e2:
            print(f"Error with both requirement files: {e2}")
            print("Continuing with already installed packages...")
    
    print("Starting FastAPI server...")
    # Run the main.py file
    subprocess.run([sys.executable, "main.py"])

if __name__ == "__main__":
    main()