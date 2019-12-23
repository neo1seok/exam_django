from django.db import models

class NeoModel(models.Model):
	uid = models.CharField(max_length=16, null=True,editable=False)

	def save(self):
		print(self._meta.object_name)
		# Book

		print(self._meta.model_name)
		# book

		print(self._meta.app_label)

		models.Model.save(self)
		self.uid = f"chn_{self.id}"
		models.Model.save(self,update_fields=["uid"])
