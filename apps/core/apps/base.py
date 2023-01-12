from importlib import import_module

from django.apps import AppConfig


class BaseConfig(AppConfig):

    def ready(self) -> None:
        super().ready()

        try:
            import_module(f'{self.name}.receivers')

        except ModuleNotFoundError:
            pass
