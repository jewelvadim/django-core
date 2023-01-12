from django.db import models
from django.utils.timezone import now


class CreatedMixin(models.Model):
	created_at = models.DateTimeField(verbose_name='Дата и время создания', default=now)

	class Meta:
		abstract = True
