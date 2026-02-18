"""
Script to run the algorithmic trading platform frontend
"""
import subprocess
import sys
import os
import time

def main():
    """Main function to start the frontend server"""
    print("Starting Algorithmic Trading Platform Frontend...")
    
    # Change to frontend directory
    frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
    os.chdir(frontend_dir)
    
    print("Installing frontend dependencies...")
    # Install dependencies
    subprocess.run(["npm", "install"], check=True)
    
    print("Starting Next.js development server...")
    # Run the Next.js dev server
    subprocess.run(["npm", "run", "dev"])

if __name__ == "__main__":
    main()