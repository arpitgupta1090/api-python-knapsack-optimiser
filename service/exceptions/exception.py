from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def validation_exception_handler(request: Request, exc):
    errors = list()
    for elem in exc.errors():
        error_code = "KSO_INPUT_0000"
        error_message = f"Failed to execute {request.method} on {request.url}: {elem.get('msg')}"
        error_target = "request body"
        error_type = "invalid"

        if elem.get('type') == "value_error.missing":
            error_code = "KSO_INPUT_0001"
            error_type = "required"
            if elem.get('loc'):
                error_target = "-->".join(map(str, elem.get('loc')))

        if "type_error" in elem.get('type'):
            error_code = "KSO_INPUT_0002"
            error_type = "invalid type"
            if elem.get('loc'):
                error_target = "-->".join(map(str, elem.get('loc')))

        if elem.get('type') == "value_error.jsondecode":
            error_code = "KSO_INPUT_0003"
            error_type = "invalid request body"
            error_target = elem.get("ctx").get("doc").split("\n")[elem.get("ctx").get("lineno") - 1]
        errors.append(
            jsonable_encoder(
                    {
                        "code": error_code,
                        "message": error_message,
                        "target": error_target,
                        "type": error_type,
                    }
                )
            )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"errors": errors}
    )


def http_exception_handler(request, exc):
    errors = list()
    error_message = f"Failed to execute {request.method} on {request.url}: {exc.detail}"
    error_code = "KSO_GENERAL_0000"
    error_target = "input"
    error_type = "invalid"
    errors.append(
        jsonable_encoder(
            {
                "code": error_code,
                "message": error_message,
                "target": error_target,
                "type": error_type,
            }
        )
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"errors": errors}
    )


def internal_exception_handler(request, exc):
    errors = list()
    error_message = f"Failed to execute {request.method} on {request.url}: {repr(exc)}"
    error_code = "KSO_INTERNAL_0000"
    error_target = "server"
    error_type = "internal error"
    errors.append(
        jsonable_encoder(
            {
                "code": error_code,
                "message": error_message,
                "target": error_target,
                "type": error_type,
            }
        )
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"errors": errors}
    )
