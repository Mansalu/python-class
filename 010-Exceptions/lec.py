# Exceptions

class LoganError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise LoganError("Something bad happened")
except LoganError as e:
    print(e.message)