import src.util.helper.interface as module_helper_interface
class Response(module_helper_interface.EqualAttributes):
    def __init__(self, success: bool=True, message: str=None, data: dict=None):
        self.success = success
        self.message = message
        self.data = data