import src.service.file as module_service_file
import src.entities.model.controller.import_words as module_model_import_words


class ImportWordsUsecase:

    def __init__(self, file_service:module_service_file.FileService) -> None:
        self.file_service = file_service

    def import_words(self, request: module_model_import_words.ImportWordsRequest) -> module_model_import_words.ImportWordsResponse:
        file_dir = request.file_dir
        self.file_service.move_to_processing(file_dir)
        pass