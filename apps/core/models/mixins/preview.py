from django.db import models


class PreviewMixin(models.Model):
	preview = models.ImageField(verbose_name='Превью', blank=True, null=True)

	class Meta:
		abstract = True
