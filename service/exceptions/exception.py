from fastapi import Request, status
from fastapi.responses import JSONResponse
from service.logger.error_logger import logger
from service.exceptions.formater import exception_format_builder


def validation_exception_handler(request: Request, exc):
    errors = []
    for elem in exc.errors():
        error = exception_format_builder("ValidationExceptionFormat", request, elem).generate()

        if elem.get('type') == "value_error.missing":
            error = exception_format_builder("ValidationExceptionValueFormat", request, elem).generate()

        if "type_error" in elem.get('type'):
            error = exception_format_builder("ValidationExceptionTypeFormat", request, elem).generate()

        if elem.get('type') == "value_error.jsondecode":
            error = exception_format_builder("ValidationExceptionJsonFormat", request, elem).generate()

        errors.append(error)

    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"errors": errors})


def http_exception_handler(request, exc):
    errors = exception_format_builder("HTTPExceptionFormat", request, exc).generate()
    return JSONResponse(status_code=exc.status_code, content={"errors": errors})


def internal_exception_handler(request, exc):
    logger.error(f"{repr(exc)}")
    errors = exception_format_builder("InternalExceptionFormat", request, exc).generate()
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"errors": errors})
