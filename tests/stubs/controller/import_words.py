import src.entities.model.usecase.import_words as module_model_usecase_import_words
import src.entities.model.controller.import_words as module_model_controller_import_words

class ImportWordsUsecaseStub(module_model_usecase_import_words.ImportWordsUsecaseBase):
    def import_words(self, request: module_model_controller_import_words.ImportWordsRequest) -> module_model_controller_import_words.ImportWordsResponse:
        return module_model_controller_import_words.ImportWordsResponse(
            file_list=['any_file_dir'],
            description_imported=2,
            words_imported=2
        )