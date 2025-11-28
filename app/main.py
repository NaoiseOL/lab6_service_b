from fastapi import FastAPI
import httpx, os

app = FastAPI(title="Service B - Proxy API")
SERVICE_A_BASE_URL = os.getenv("SERVICE_A_BASE_URL", "http://localhost:8001")

@app.get("/api/proxy-greet")
def call_service_a(name: str = "world"):
    url = f"{SERVICE_A_BASE_URL}/api/greet/{name}"
    with httpx.Client() as client:
        r = client.get(url)
    return {"service_b": True, "service_a_response": r.json()}

