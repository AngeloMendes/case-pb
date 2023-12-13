from fastapi.testclient import TestClient
from app import server

client = TestClient(server.app)