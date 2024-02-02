from abc import ABC, abstractmethod
import src.model.http.request as module_request
import src.model.http.response as module_response

class BaseController(ABC):
    @abstractmethod
    def handle(self, request: module_request.Request) -> module_response.Response:
        pass