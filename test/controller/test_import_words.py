import unittest.mock as mock
import src.controller.import_words as module_controller_import_words
import src.entities.model.http.request as module_request
import src.entities.model.controller.import_words as module_model_import_words
import src.entities.adapter.import_words as module_adapter_import_words
import src.business.import_words as module_business_import_words
import src.util.helper.response as module_helper_response

class SutTypes:
    def __init__(self, sut:module_controller_import_words.ImportWordsController, adapter:module_adapter_import_words.ImportWordsAdapter):
        self.sut = sut
        self.adapter = adapter

def get_sut_types(
        adapter:module_adapter_import_words.ImportWordsAdapter=module_adapter_import_words.ImportWordsAdapter(),
        business=module_business_import_words.ImportWordsBusiness
    ):
    sut = module_controller_import_words.ImportWordsController(adapter=adapter,business=business)
    return SutTypes(sut=sut, adapter=adapter)

def test_request_is_null():
    sut_types = get_sut_types()
    sut = sut_types.sut
    response = sut.handle(None)
    assert response == module_helper_response.null_request_response()

def test_request_has_no_fields():
    sut_types = get_sut_types()
    sut = sut_types.sut
    response = sut.handle(request=module_request.Request())
    assert response == module_helper_response.no_fields_response()

def test_request_any_required_fields_are_empty():
    sut_types = get_sut_types()
    sut = sut_types.sut
    response = sut.handle(request=module_request.Request(body={'file_dir':None}))
    assert response == module_helper_response.any_required_fields_empty_response()

def test_check_import_word_adapter_is_beign_called():
    import_words_adapter = mock.MagicMock()
    sut_types = get_sut_types(adapter=import_words_adapter)
    sut = sut_types.sut
    request = module_request.Request(body={'file_dir':'any_file_dir'})
    sut.handle(request=request)
    import_words_adapter.adapt.assert_called_once_with(request=request)

def test_handle_exception_when_import_word_adapter_throws():
    import_words_adapter = mock.MagicMock()
    import_words_adapter.adapt.side_effect = Exception('any_error')
    sut_types = get_sut_types(adapter=import_words_adapter)
    sut = sut_types.sut
    request = module_request.Request(body={'file_dir':'any_file_dir'})
    response = sut.handle(request=request)
    assert response == module_helper_response.generic_error_response()

def test_check_import_word_business_is_beign_called():
    import_words_business = mock.MagicMock()
    sut_types = get_sut_types(business=import_words_business)
    sut = sut_types.sut
    expected = module_model_import_words.ImportWordsRequest(file_dir='any_file_dir')
    request = module_request.Request(body={'file_dir':'any_file_dir'})
    sut.handle(request=request)
    import_words_business.import_words.assert_called_once_with(expected)

def test_handle_exception_when_import_word_business_throws():
    adapter = mock.MagicMock()
    business = mock.MagicMock()
    adapter.return_value.adapt.return_value = module_model_import_words.ImportWordsRequest(file_dir='any_file_dir')
    business.import_words.side_effect = Exception('any_error')
    sut_types = get_sut_types(adapter=adapter, business=business)
    sut = sut_types.sut
    request = module_request.Request(body={'file_dir':'any_file_dir'})
    response = sut.handle(request=request)
    assert response == module_helper_response.generic_error_response()
