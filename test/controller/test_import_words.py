from src.controller.import_words import ImportWordsController

import src.util.constant as module_constant

def test_request_is_null():
    sut = ImportWordsController()
    response = sut.handle(None)
    assert response.success == False
    assert response.message == module_constant.DEFAULT_MESSAGE_RESPONSE_NULL_REQUEST
    assert response.data == None