import src.controller.base as module_base_controller

import src.model.http.request as module_request
import src.model.http.response as module_response

import src.util.constant as module_constant

class ImportWordsController(module_base_controller.BaseController):
    def handle(self, request: module_request.Request) -> module_response.Response:
        return module_response.Response(False, module_constant.DEFAULT_MESSAGE_RESPONSE_NULL_REQUEST)