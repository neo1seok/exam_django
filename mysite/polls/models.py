import datetime
from django.utils import timezone
from django.db import models


# Create your models here.
from .comm.neo_models import NeoModel


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.question_text
	
	# def was_published_recently(self):
	#     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(NeoModel):
	#uid = models.CharField(max_length=16, null=True,editable=False)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	_prefix ="cpn"
	
	# def save(self):
	# 	print(self._meta.object_name)
	# 	# Book
	#
	# 	print(self._meta.model_name)
	# 	# book
	#
	# 	print(self._meta.app_label)
	#
	#
	# 	super(Choice, self).save()
	# 	print("save id after", self.id)
	# 	self.uid = f"chn_{self.id}"
	# 	super(Choice, self).save(update_fields=["uid"])

	
	def __str__(self):
		return self.choice_text
