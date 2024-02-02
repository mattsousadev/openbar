import src.model.http.request as module_request
import src.model.controller.import_words as module_controller_import_words

class ImportWordsAdapter():
    def adapt(self, request: module_request.Request) -> module_controller_import_words.ImportWordsRequest:
        file_path = request.body['file_dir']
        return module_controller_import_words.ImportWordsRequest(file_path)