class Request():
    def __init__(self, body: dict=None, headers: dict=None):
        self.body = body
        self.headers = headers
