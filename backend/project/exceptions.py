class EmptyListResponseException(Exception):
    def __init__(self, message):
        self.message = message


class BadRequestException(Exception):
    def __init__(self, message):
        self.message = message


class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message
