from django.conf import settings

from backoff import expo, on_exception
from requests import get
from requests.exceptions import ConnectionError, ConnectTimeout


@on_exception(wait_gen=expo, exception=(ConnectionError, ConnectTimeout), max_tries=10)
def send_tg_message(title: str, message: str) -> None:
    text = f'{title}\n\n{message}'

    if settings.TG_BOT_TOKEN and settings.TG_CHAT:
        get(f'https://api.telegram.org/bot{settings.TG_BOT_TOKEN}/sendMessage?chat_id={settings.TG_CHAT}&text={text}')
