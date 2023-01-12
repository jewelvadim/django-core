from django.db import models


class SlugMixin(models.Model):
	slug = models.SlugField(verbose_name='Адрес в строке браузера', max_length=255, unique=True)

	class Meta:
		abstract = True
