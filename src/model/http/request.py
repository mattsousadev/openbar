class Request():
    def __init__(self, body: dict[str:str]=None, headers: dict[str:str]=None):
        self.body = body
        self.headers = headers
