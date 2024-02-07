import src.service.file as module_service_file
import src.entities.model.controller.import_words as module_model_import_words
import src.entities.exception.app as module_model_exception
import src.service.word as module_service_word
import src.util.constant as module_constant

# TODO: Create base class for usecase
class ImportWordsUsecase:

    def __init__(self, file_service:module_service_file.FileService, word_service:module_service_word.WordService) -> None:
        self.file_service = file_service
        self.word_service = word_service

    def import_words(self, request: module_model_import_words.ImportWordsRequest) -> module_model_import_words.ImportWordsResponse:
        file_dir = request.file_dir
        if not self.file_service.exists(file_dir):
            # TODO: create custom exception
            raise module_model_exception.AppException(module_constant.DEFAULT_EXCEPTION_DIRECTORY_NOT_FOUND)
        file_paths = self.file_service.move_to_processing(file_dir)
        if len(file_paths) == 0:
            raise module_model_exception.AppException(module_constant.DEFAULT_EXCEPTION_NO_FILE_MOVED)
        try:    
            for file_path in file_paths:
                # TODO: read file
                table_words = self.file_service.read_words_file(file_path)
                # TODO: persist words
                for row in table_words.items():
                    self.word_service.persist_words(row)
                # TODO: move file to processed
        except:
            raise module_model_exception.AppException(module_constant.DEFAULT_EXCEPTION_ERROR_READING_WORDS_FILE)
        # TODO: encode file to base64
        # TODO: persist base64 file
        # TODO: return response
        pass