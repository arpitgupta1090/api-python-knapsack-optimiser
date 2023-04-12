import uvicorn
from fastapi import FastAPI
import api

description = """
**This API provides a optimised output for the Knapsack problem**

* **Home Page** (You can read the API documentation on the home page "/". 
                Sample Request and Response are provided on the right side).
* **Test** (use **/test** endpoint to test the API using sample data or your own data).
"""

app = FastAPI(
    title="Knapsack Optimiser",
    description=description,
    version="0.1",
    contact={
        "name": "Arpit Gupta",
        "email": "arpitgupta1090@gmail.com",
    },
    docs_url="/test",
    redoc_url="/"
)
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