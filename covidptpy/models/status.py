from covidptpy.models.base import Base


class Status(Base):

    def __init__(self, response_code, status_text):
        super().__init__(response_code)
        self.status_text = status_text

