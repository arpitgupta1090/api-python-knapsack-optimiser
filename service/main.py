import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from service import api
from service.exceptions.exception import (validation_exception_handler,
                                          http_exception_handler,
                                          internal_exception_handler,
                                          )

app = FastAPI(
    docs_url="/tryit",
    redoc_url="/",
)

description = """
**This API provides a optimised output for the Knapsack problem**

* **Home Page** (You can read the API documentation on the home page "/". 
                Sample Request and Response are provided on the right side).
* **Try It** (use **/tryit** endpoint to test the API using sample data or your own data).
"""


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Knapsack Optimiser",
        version="0.1",
        description=description,
        routes=app.routes,
        contact={
            "name": "Arpit Gupta",
            "email": "arpitgupta1090@gmail.com",
        },
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://cdn.pixabay.com/photo/2017/09/26/21/54/logo-2790253_1280.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
app.include_router(api.router)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(Exception, internal_exception_handler)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=5000)
