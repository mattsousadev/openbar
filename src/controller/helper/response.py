import src.model.http.response as module_response

import src.util.constant as module_constant

def null_request_response():
    return module_response.Response(
        success=False
        , message=module_constant.DEFAULT_MESSAGE_RESPONSE_NULL_REQUEST
        , data=None
    )

def no_fields_response():
    return module_response.Response(
        success=False
        , message=module_constant.DEFAULT_MESSAGE_RESPONSE_NO_FIELDS
        , data=None
    )