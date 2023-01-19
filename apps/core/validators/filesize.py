from typing import NoReturn

from django.core.exceptions import ValidationError
from django.core.files import File
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    size: int
    message: str
    code: str

    def __init__(self, size: int) -> None:
        self.size = size
        self.message = f'Максимальный размер файла не должен превышать {self.size / (1024 * 1024)} MB'
        self.code = 'invalid_size'

    def __call__(self, value: File) -> NoReturn:

        if value.size > self.size:
            raise ValidationError(message=self.message, code=self.code)
