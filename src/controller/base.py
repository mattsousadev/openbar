from abc import ABC, abstractmethod
import src.entities.model.http.request as module_request
import src.entities.model.http.response as module_response

class BaseController(ABC):
    @abstractmethod
    def handle(self, request: module_request.Request) -> module_response.Response:
        pass