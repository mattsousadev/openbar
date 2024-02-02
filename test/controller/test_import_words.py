from src.controller.import_words import ImportWordsController
import unittest.mock as mock
import src.model.http.request as module_request
import src.entities.adapter.import_words as module_adapter_import_words
import src.util.helper.response as module_helper_response
class SutTypes:
    def __init__(self, sut:ImportWordsController, adapter:module_adapter_import_words.ImportWordsAdapter):
        self.sut = sut
        self.adapter = adapter

def get_sut_types(adapter:module_adapter_import_words.ImportWordsAdapter=module_adapter_import_words.ImportWordsAdapter()):
    sut = ImportWordsController(adapter=adapter)
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

def test_check_parameter_builder_is_beign_called():
    import_words_adapter = mock.MagicMock()
    sut_types = get_sut_types(adapter=import_words_adapter)
    sut = sut_types.sut
    request = module_request.Request(body={'file_dir':'any_file_dir'})
    sut.handle(request=request)
    import_words_adapter.adapt.assert_called_once_with(request=request)