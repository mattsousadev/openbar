import unittest as module_unittest
import unittest.mock as module_unittest_mock
import src.controller.import_words as module_controller_import_words
import src.entities.model.http.request as module_request
import src.entities.model.controller.import_words as module_model_controller_import_words
import src.entities.adapter.import_words as module_adapter_import_words
import src.entities.model.usecase.import_words as module_model_usecase_import_words
import src.util.helper.response as module_helper_response
import src.entities.exception.app as module_model_exception

import tests.stubs.controller.import_words as module_stubs_import_words

class SutTypes:
    def __init__(self, sut:module_controller_import_words.ImportWordsController, adapter:module_adapter_import_words.ImportWordsAdapter):
        self.sut = sut
        self.adapter = adapter

def get_sut_types(
        adapter:module_adapter_import_words.ImportWordsAdapter=module_adapter_import_words.ImportWordsAdapter(),
        usecase:module_model_usecase_import_words.ImportWordsUsecaseBase=module_stubs_import_words.ImportWordsUsecaseStub()
    ):
    sut = module_controller_import_words.ImportWordsController(adapter=adapter,usecase=usecase)
    return SutTypes(sut=sut, adapter=adapter)

class TestImportWordController(module_unittest.TestCase):
    def test_request_is_null(self):
        sut_types = get_sut_types()
        sut = sut_types.sut
        response = sut.handle(None)
        assert response == module_helper_response.null_request_response()

    def test_request_has_no_fields(self):
        sut_types = get_sut_types()
        sut = sut_types.sut
        response = sut.handle(request=module_request.Request())
        assert response == module_helper_response.no_fields_response()

    def test_request_any_required_fields_are_empty(self):
        sut_types = get_sut_types()
        sut = sut_types.sut
        response = sut.handle(request=module_request.Request(body={'file_dir':None}))
        assert response == module_helper_response.any_required_fields_empty_response()

    def test_check_import_word_adapter_is_beign_called(self):
        import_words_adapter = module_unittest_mock.MagicMock()
        sut_types = get_sut_types(adapter=import_words_adapter)
        sut = sut_types.sut
        request = module_request.Request(body={'file_dir':'any_file_dir'})
        sut.handle(request=request)
        import_words_adapter.adapt.assert_called_once_with(request=request)

    def test_handle_exception_when_import_word_adapter_throws(self):
        import_words_adapter = module_unittest_mock.MagicMock()
        import_words_adapter.adapt.side_effect = Exception('any_error')
        sut_types = get_sut_types(adapter=import_words_adapter)
        sut = sut_types.sut
        request = module_request.Request(body={'file_dir':'any_file_dir'})
        response = sut.handle(request=request)
        assert response == module_helper_response.generic_error_response()

    def test_check_import_word_usecase_is_beign_called(self):
        import_words_usecase = module_unittest_mock.MagicMock()
        sut_types = get_sut_types(usecase=import_words_usecase)
        sut = sut_types.sut
        expected = module_model_controller_import_words.ImportWordsRequest(file_dir='any_file_dir')
        request = module_request.Request(body={'file_dir':'any_file_dir'})
        sut.handle(request=request)
        import_words_usecase.import_words.assert_called_once_with(expected)

    def test_handle_exception_when_import_word_usecase_throws(self):
        adapter = module_unittest_mock.MagicMock()
        usecase = module_unittest_mock.MagicMock()
        adapter.return_value.adapt.return_value = module_model_controller_import_words.ImportWordsRequest(file_dir='any_file_dir')
        usecase.import_words.side_effect = Exception('any_error')
        sut_types = get_sut_types(adapter=adapter, usecase=usecase)
        sut = sut_types.sut
        request = module_request.Request(body={'file_dir':'any_file_dir'})
        response = sut.handle(request=request)
        assert response == module_helper_response.generic_error_response()

    def test_handle_app_exception_when_import_word_usecase_throws(self):
        adapter = module_unittest_mock.MagicMock()
        usecase = module_unittest_mock.MagicMock()
        adapter.return_value.adapt.return_value = module_model_controller_import_words.ImportWordsRequest(file_dir='any_file_dir')
        usecase.import_words.side_effect = module_model_exception.AppException('Any app exception')
        sut_types = get_sut_types(adapter=adapter, usecase=usecase)
        sut = sut_types.sut
        request = module_request.Request(body={'file_dir':'any_file_dir'})
        response = sut.handle(request=request)
        assert response == module_helper_response.app_error_response('Any app exception')
    
    def test_return_success(self):
        sut_types = get_sut_types()
        sut = sut_types.sut
        request = module_request.Request(body={'file_dir':'any_file_dir'})
        response = sut.handle(request=request)
        assert response == module_helper_response.ok_response({
            'file_list': ['any_file_dir'],
            'description_imported': 2,
            'words_imported':2
        })