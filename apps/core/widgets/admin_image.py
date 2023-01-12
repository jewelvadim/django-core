from django.contrib.admin.widgets import AdminFileWidget


class AdminImageWidget(AdminFileWidget):
	template_name = 'admin/admin_image_widget.html'

	def get_context(self, name, value, attrs):
		context = super().get_context(name, value, attrs)

		context['widget']['attrs'].setdefault('width', 250)
		context['widget']['attrs'].setdefault('height', 250)

		return context
