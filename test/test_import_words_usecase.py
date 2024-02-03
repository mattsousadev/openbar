import unittest as module_unittest
import unittest.mock as module_unittest_mock
import src.usecase.import_words as module_usecase_import_words
import src.entities.model.controller.import_words as module_model_import_words

class TestImportWordUsecase(module_unittest.TestCase):
    def test_check_file_service_is_beign_called(self):
        file_service = module_unittest_mock.MagicMock()
        sut = module_usecase_import_words.ImportWordsUsecase(file_service=file_service)
        request = module_model_import_words.ImportWordsRequest(file_dir="any_file_dir")
        sut.import_words(request)
        file_service.move_to_processing.assert_called_once_with("any_file_dir")
        