from os.path import join, getmtime
from time import gmtime, strftime

from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def sstatic(filepath: str) -> str:
	result = f'{settings.STATIC_URL}{filepath}'
	full_path = join(settings.STATIC_ROOT, filepath)

	try:
		mtime = strftime('%d.%m.%Y-%H.%M.%S', gmtime(getmtime(full_path)))

	except OSError:
		pass

	else:
		result += f'?{mtime}'

	return result


@register.filter()
def prettify_phone(v: str) -> str:
	return f'{v[:2]} ({v[2:5]}) {v[5:8]}-{v[8:10]}-{v[10:12]}'
