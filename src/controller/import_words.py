import src.controller.base as module_base_controller

import src.model.http.request as module_request
import src.model.http.response as module_response

import src.controller.helper.response as module_helper_response

class ImportWordsController(module_base_controller.BaseController):

    def __init__(self):
        super().__init__()
        self.required_fields = {
            'body':['file_dir']
        }
    
    def handle(self, request: module_request.Request) -> module_response.Response:
        if request == None:
            return module_helper_response.null_request_response()
        if not request.body and not request.headers:
            return module_helper_response.no_fields_response()
        for field in self.required_fields['body']:
            if request.body[field] == None or request.body[field] == '':
                return module_helper_response.any_required_fields_empty_response()
        for field in self.required_fields['headers']:
            if request.headers[field] == None or request.headers[field] == '':
                return module_helper_response.any_required_fields_empty_response()
        return None