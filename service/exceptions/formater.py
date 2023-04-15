from abc import ABC, abstractmethod
import sys


class ExceptionFormat(ABC):

    def __init__(self, input_request, error):
        self.input_request = input_request
        self.error = error

    @abstractmethod
    def generate(self):
        pass


class HTTPExceptionFormat(ExceptionFormat):

    def generate(self):
        return [
            {"code": "KSO_GENERAL_0000",
             "message": f"Failed to execute {self.input_request.method} on {self.input_request.url}: {self.error.detail}",
             "target": "input",
             "type": "invalid"
             }
        ]


class InternalExceptionFormat(ExceptionFormat):

    def generate(self):
        return [
            {"code": "KSO_INTERNAL_0000",
             "message": f"Failed to execute {self.input_request.method} on {self.input_request.url}",
             "target": "server",
             "type": "internal error"
             }
        ]


class ValidationExceptionFormat(ExceptionFormat):

    def generate(self):
        return {
            "code": "KSO_INPUT_0000",
            "message": f"Failed to execute {self.input_request.method} on "
                       f"{self.input_request.url}: {self.error.get('msg')}",
            "target": "request body",
            "type": "invalid"
        }


class ValidationExceptionValueFormat(ExceptionFormat):

    def generate(self):
        if self.error.get('loc'):
            error_target = "-->".join(map(str, self.error.get('loc')))
        else:
            error_target = "request body"
        return {
            "code": "KSO_INPUT_0001",
            "message": f"Failed to execute {self.input_request.method} on "
                       f"{self.input_request.url}: {self.error.get('msg')}",
            "target": error_target,
            "type": "required"
        }


class ValidationExceptionTypeFormat(ExceptionFormat):

    def generate(self):
        if self.error.get('loc'):
            error_target = "-->".join(map(str, self.error.get('loc')))
        else:
            error_target = "request body"
        return {
            "code": "KSO_INPUT_0002",
            "message": f"Failed to execute {self.input_request.method} on "
                       f"{self.input_request.url}: {self.error.get('msg')}",
            "target": error_target,
            "type": "invalid type"
        }


class ValidationExceptionJsonFormat(ExceptionFormat):

    def generate(self):
        return {
            "code": "KSO_INPUT_0003",
            "message": f"Failed to execute {self.input_request.method} on "
                       f"{self.input_request.url}: {self.error.get('msg')}",
            "target": self.error.get("ctx").get("doc").split("\n")[self.error.get("ctx").get("lineno") - 1],
            "type": "invalid request body"
        }


def exception_format_builder(error_class_name, input_request, error):
    class_name = getattr(sys.modules[__name__], error_class_name)
    return class_name(input_request, error)
