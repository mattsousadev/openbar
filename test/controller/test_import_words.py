from src.controller.import_words import ImportWordsController
import src.model.http.request as module_request

import src.util.constant as module_constant

def test_request_is_null():
    sut = ImportWordsController()
    response = sut.handle(None)
    assert response.success == False
    assert response.message == module_constant.DEFAULT_MESSAGE_RESPONSE_NULL_REQUEST
    assert response.data == None

def test_request_has_no_fields():
    sut = ImportWordsController()
    response = sut.handle(request=module_request.Request())
    assert response.success == False
    assert response.message == module_constant.DEFAULT_MESSAGE_RESPONSE_NO_FIELDS
    assert response.data == None

def test_request_any_required_fields_are_empty():
    sut = ImportWordsController()
    response = sut.handle(request=module_request.Request(body={'file_dir':None}))
    assert response.success == False
    assert response.message == module_constant.DEFAULT_MESSAGE_RESPONSE_SOME_REQUIRED_FIELDS_EMPTY
    assert response.data == None