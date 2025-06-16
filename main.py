from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_main_page():
    return {"detail": "check status /status"}

@app.get("/status")
def get_status():
    return {"status": "online"}