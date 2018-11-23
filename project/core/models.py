from django.db import models

# Create your models here.
from django.db import models

class Tag(models.Model):
    description = models.CharField(max_length=150)
    icon = models.CharField(max_length=500)


class Payment(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	description = models.CharField(max_length=150)
	value = models.FloatField()
	initial_date = models.DateField()
	final_date = models.DateField()
	is_renda = models.BooleanField()
	is_continuous = model.BooleanField() 

	def __str__(self):
		return self.description

class PaymentCustom(models.Model):
	payment = models.ForeignKey(Payment, on_delete = models.CASCADE)
	date    = model.DateField()