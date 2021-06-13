class Status:

    def __init__(self, response_code, status_text):
        self.response_code = response_code
        self.status_text = status_text

    def __str__(self):
        return self.status_text
