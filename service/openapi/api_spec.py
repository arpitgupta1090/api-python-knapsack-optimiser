from service.openapi.sample_data import error_body, response_body

additional_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "sample": {
                        "value": response_body
                    }
                }
            }
        }
    },
    "400": {
        "description": "Request validation error",
        "content": {
            "application/json": {
                "schema": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["code",
                                     "message",
                                     "target",
                                     "type"],
                        "properties": {
                            "code": {"type": "string",
                                     "title": "error code"},
                            "message": {"type": "string",
                                        "title": "error message"},
                            "target": {"type": "string",
                                       "title": "error location"},
                            "type": {"type": "string",
                                     "title": "error type"}

                        }
                    },

                },
                "examples": {
                    "sample": {
                        "value": error_body
                    }
                }
            }
        }
    },
}
