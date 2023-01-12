from django.db import models


class OrderMixin(models.Model):
	order = models.PositiveSmallIntegerField(
		verbose_name='Порядок вывода',
		default=1,
		help_text='Меньше число - больше вес',
	)

	class Meta:
		abstract = True
		ordering = ['order']
