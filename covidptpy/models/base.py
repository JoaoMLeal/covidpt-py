class Base:

    def __init__(self, response_code):
        self.response_code = response_code

    def __str__(self):
        return str(self.response_code)
