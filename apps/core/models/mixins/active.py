from django.db import models

from apps.core.managers import ActiveManager


class ActiveMixin(models.Model):
	is_active = models.BooleanField(
		verbose_name='Активный?',
		default=True,
		help_text='Вместо удаления элемента, снимите галочку',
	)

	objects = models.Manager()
	active_objects = ActiveManager()

	class Meta:
		abstract = True
