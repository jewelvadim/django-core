from django.db import models


class TitleMixin(models.Model):
	title = models.CharField(verbose_name='Название', max_length=255)

	class Meta:
		abstract = True

	def __str__(self) -> str:
		return str(self.title)
