from os.path import join
from uuid import uuid4

from django.db.models import Model
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename:
	_path: str

	def __init__(self, sub_path: str = '') -> None:
		self._path = sub_path

	def __call__(self, instance: Model, filename: str) -> str:
		self._path = self._path or type(instance).__name__.lower()

		extension = filename.split('.')[-1]
		filename = f'{uuid4().hex}.{extension}'

		return join(self._path, filename)
