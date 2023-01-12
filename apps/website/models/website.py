from django.db import models

from ckeditor.fields import RichTextField
from solo.models import SingletonModel


class Website(SingletonModel):
    seo_title = models.CharField(verbose_name='СЕО-заголовок страницы', max_length=255, blank=True)

    seo_description = models.TextField(verbose_name='СЕО-описание страницы', blank=True)

    policy = RichTextField(verbose_name='Политика конфиденциальности', blank=True)

    class Meta:
        verbose_name = 'Глобальные настройки'
