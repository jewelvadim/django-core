from django.db import models


class DescriptionMixin(models.Model):
	description = models.TextField(verbose_name='Описание', blank=True)

	class Meta:
		abstract = True
