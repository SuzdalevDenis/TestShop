from re import fullmatch
from ulid import parse, ULID


class ULIDConverter:
    regex = r'[a-z, A-Z, 0-9]{24}'

    def to_python(self, value):
        if fullmatch((self.regex, value)) is None:
            raise ValueError
        return parse(value.upper())

    def to_url(self, value: ULID):
        return value.str
