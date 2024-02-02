class Response():
    def __init__(self, success: bool=True, message: str=None, data: dict=None):
        self.success = success
        self.message = message
        self.data = data