import src.controller.base as module_base_controller
import src.entities.exception.app as module_model_exception
import src.entities.model.http.request as module_request
import src.entities.model.http.response as module_response
import src.util.helper.response as module_helper_response
import src.entities.adapter.import_words as module_adapter_import_words
import src.usecase.import_words as module_usecase_import_words

class ImportWordsController(module_base_controller.BaseController):

    def __init__(self, 
            adapter: module_adapter_import_words.ImportWordsAdapter, 
            usecase:module_usecase_import_words.ImportWordsUsecase
        ):
        super().__init__()
        self.adapter = adapter
        self.usecase = usecase
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
        if 'headers' in self.required_fields and request.headers != None:
            for field in self.required_fields['headers']:
                if request.headers[field] == None or request.headers[field] == '':
                    return module_helper_response.any_required_fields_empty_response()
        try:
            import_word_request = self.adapter.adapt(request=request)
            response = self.usecase.import_words(import_word_request)
            return response
        except module_model_exception.AppException as e:
            return module_helper_response.app_error_response(e.message)
        except:
            return module_helper_response.generic_error_response()