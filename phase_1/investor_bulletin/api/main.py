import os
import sys
from uvicorn import run
from fastapi import FastAPI

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from routes import init_routes
app = init_routes(FastAPI())

if __name__ == "__main__":
    run("api.main:app")
