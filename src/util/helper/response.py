import src.entities.model.http.response as module_response

import src.util.constant as module_constant

# TODO: Create a factory class for response

def null_request_response() -> module_response.Response:
    return module_response.Response(
        success=False
        , message=module_constant.DEFAULT_MESSAGE_RESPONSE_NULL_REQUEST
        , data=None
    )

def no_fields_response() -> module_response.Response:
    return module_response.Response(
        success=False
        , message=module_constant.DEFAULT_MESSAGE_RESPONSE_NO_FIELDS
        , data=None
    )

def any_required_fields_empty_response() -> module_response.Response:
    return module_response.Response(
        success=False
        , message=module_constant.DEFAULT_MESSAGE_RESPONSE_SOME_REQUIRED_FIELDS_EMPTY
        , data=None
    )

def generic_error_response() -> module_response.Response:
    return module_response.Response(
        success=False
        , message=module_constant.DEFAULT_MESSAGE_RESPONSE_GENERIC_ERROR
        , data=None
    )

def app_error_response(message:str) -> module_response.Response:
    return_message = module_constant.DEFAULT_MESSAGE_RESPONSE_APP_ERROR.format(message)
    return module_response.Response(
        success=False
        , message=return_message
        , data=None
    )