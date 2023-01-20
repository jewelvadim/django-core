from django.core.files.storage import default_storage
from django.db import models

from sorl.thumbnail import get_thumbnail


class PreviewMixin(models.Model):
	preview = models.ImageField(verbose_name='Превью', blank=True, null=True)

	class Meta:
		abstract = True

	def _get_preview_thumbnail(self, geometry_string: str, crop: str = 'noop', quality: int = 100) -> str:
		preview = ''

		if self.preview:
			thumbnail = get_thumbnail(file_=self.preview, geometry_string=geometry_string, crop=crop, quality=quality)
			preview = default_storage.url(name=thumbnail)

		return preview
