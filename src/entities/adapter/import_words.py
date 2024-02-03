import src.entities.model.http.request as module_request
import src.entities.model.controller.import_words as module_model_import_words

class ImportWordsAdapter():
    def adapt(self, request: module_request.Request) -> module_model_import_words.ImportWordsRequest:
        file_path = request.body['file_dir']
        return module_model_import_words.ImportWordsRequest(file_path)