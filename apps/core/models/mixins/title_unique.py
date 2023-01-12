from django.db import models


class TitleUniqueMixin(models.Model):
	title = models.CharField(verbose_name='Название', max_length=255, unique=True)

	class Meta:
		abstract = True
		constraints = [
			models.UniqueConstraint(fields=('title',), condition=~models.Q(title=''), name='unique_title'),
		]

	def __str__(self) -> str:
		return str(self.title)
