from django.db.models import Manager, Model, QuerySet


class ActiveManager(Manager):

	def get_queryset(self) -> QuerySet[Model]:
		return super().get_queryset().filter(is_active=True)
