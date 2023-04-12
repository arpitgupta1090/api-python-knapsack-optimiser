import uvicorn
from fastapi import FastAPI
import api

app = FastAPI()
app.include_router(api.router)


@app.get("/ping", tags=["Health check"], summary="Check if the service is operational")
def pong():
    """
    Health check
    """
    print("Ping: Pong")
    return {"ping": "pong!"}


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=5000
    )