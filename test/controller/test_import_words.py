from src.controller.import_words import ImportWordsController
import src.model.http.request as module_request

import src.util.helper.response as module_helper_response

def test_request_is_null():
    sut = ImportWordsController()
    response = sut.handle(None)
    assert response == module_helper_response.null_request_response()

def test_request_has_no_fields():
    sut = ImportWordsController()
    response = sut.handle(request=module_request.Request())
    assert response == module_helper_response.no_fields_response()

def test_request_any_required_fields_are_empty():
    sut = ImportWordsController()
    response = sut.handle(request=module_request.Request(body={'file_dir':None}))
    assert response == module_helper_response.any_required_fields_empty_response()