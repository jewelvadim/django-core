from django.db.models import Manager, Model, QuerySet


class ActiveManager(Manager):

	def active(self) -> QuerySet[Model]:
		return self.filter(is_active=True)

	def inactive(self) -> QuerySet[Model]:
		return self.filter(is_active=False)
