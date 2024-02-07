import unittest as module_unittest
import unittest.mock as module_unittest_mock
import src.usecase.import_words as module_usecase_import_words
import src.entities.model.controller.import_words as module_model_import_words
import src.service.file as module_service_file
import src.service.word as module_service_word
import src.entities.exception.app as module_model_exception
import src.util.constant as module_constant
import src.entities.table.words as module_table_words

# TODO: Add sut types
class SutTypes:
    def __init__(self, sut:module_usecase_import_words.ImportWordsUsecase
                , file_service:module_service_file.FileService
                , word_service:module_service_word.WordService):
        self.sut = sut
        self.file_service = file_service
        self.word_service = word_service

def get_sut_types(file_service:module_service_file.FileService, word_service:module_service_word.WordService):
    sut = module_usecase_import_words.ImportWordsUsecase(file_service=file_service, word_service=word_service)
    return SutTypes(sut=sut, file_service=file_service, word_service=word_service)


class TestImportWordUsecase(module_unittest.TestCase):
    def test_check_file_service_is_beign_called(self):
        file_service = module_unittest_mock.MagicMock()
        word_service = module_unittest_mock.MagicMock()
        file_service.move_to_processing.return_value = ['any_file1', 'any_file2']
        sut_types = get_sut_types(file_service=file_service, word_service=word_service)
        sut = sut_types.sut
        request = module_model_import_words.ImportWordsRequest(file_dir="any_file_dir")
        sut.import_words(request)
        file_service.move_to_processing.assert_called_once_with("any_file_dir")
        
    def test_throw_app_error_when_file_dir_not_found(self):
        file_service = module_unittest_mock.MagicMock()
        word_service = module_unittest_mock.MagicMock()
        file_service.exists.side_effect = module_model_exception.AppException(module_constant.DEFAULT_EXCEPTION_DIRECTORY_NOT_FOUND)
        sut_types = get_sut_types(file_service=file_service, word_service=word_service)
        sut = sut_types.sut
        request = module_model_import_words.ImportWordsRequest(file_dir="any_file_dir")
        with self.assertRaises(module_model_exception.AppException) as context:
            sut.import_words(request)
        context.exception.message == module_constant.DEFAULT_EXCEPTION_DIRECTORY_NOT_FOUND
    
    def test_throw_app_error_when_no_files_moved(self):
        file_service = module_unittest_mock.MagicMock()
        word_service = module_unittest_mock.MagicMock()
        file_service.move_to_processing.return_value = []
        sut_types = get_sut_types(file_service=file_service, word_service=word_service)
        sut = sut_types.sut
        request = module_model_import_words.ImportWordsRequest(file_dir="any_file_dir")
        with self.assertRaises(module_model_exception.AppException) as context:
            sut.import_words(request)
        context.exception.message == module_constant.DEFAULT_EXCEPTION_NO_FILE_MOVED

    def test_throw_error_when_could_not_read_file(self):
        file_service = module_unittest_mock.MagicMock()
        word_service = module_unittest_mock.MagicMock()
        file_service.move_to_processing.return_value = ['any_file1', 'any_file2']
        file_service.read_words_file.side_effect = Exception('any_error')
        sut_types = get_sut_types(file_service=file_service, word_service=word_service)
        sut = sut_types.sut
        request = module_model_import_words.ImportWordsRequest(file_dir="any_file_dir")
        with self.assertRaises(module_model_exception.AppException) as context:
            sut.import_words(request)
        context.exception.message == module_constant.DEFAULT_EXCEPTION_NO_FILE_MOVED
    
    def test_check_word_service_is_beign_called(self):
        file_service = module_unittest_mock.MagicMock()
        word_service = module_unittest_mock.MagicMock()
        file_service.move_to_processing.return_value = ['any_file1', 'any_file2']
        file_service.read_words_file.return_value = module_table_words.TableWords(table=[('any_word','any_description')])
        sut_types = get_sut_types(file_service=file_service, word_service=word_service)
        sut = sut_types.sut
        request = module_model_import_words.ImportWordsRequest(file_dir="any_file_dir")
        sut.import_words(request)
        word_service.persist_words.assert_called_with(("any_word", "any_description"))
