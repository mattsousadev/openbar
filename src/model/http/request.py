import src.util.helper.interface as module_helper_interface
class Request(module_helper_interface.EqualAttributes):
    def __init__(self, body: dict[str:str]=None, headers: dict[str:str]=None):
        self.body = body
        self.headers = headers
