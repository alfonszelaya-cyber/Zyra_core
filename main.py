from fastapi import FastAPI

app = FastAPI(title="ZYRA CORE")

@app.get("/")
def root():
    return {
        "system": "ZYRA CORE",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "foundation": "loaded",
        "engines": [
            "economic_engine",
            "logistics_engine",
            "security_engine"
        ],
        "protocol": "active",
        "apps": [
            "nexo"
        ],
        "status": "healthy"
    }
