from fastapi import FastAPI

app = FastAPI(title="ZYRA CORE")

@app.get("/")
def root():
    return {"status": "ZYRA CORE RUNNING"}
