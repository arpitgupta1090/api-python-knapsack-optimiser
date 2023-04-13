from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Request, status


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = list()
    for elem in exc.errors():
        error_code = "KSO_INPUT_0000"
        error_message = elem.get('msg')
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
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"errors": errors}
    )
