from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.
class Bills(models.Model):
		PAID = 'PD'
		UNPAID = 'NP'
		STATUS_CHOICES = (
			(PAID, 'Paid'),
			(UNPAID, 'Unpaid'),
			)

		month = models.CharField(max_length = 120)
		billType = models.CharField(max_length = 120)
		amountDue = models.DecimalField(max_digits=19, decimal_places=2)
		status  =  models.CharField(
			max_length=2,
			choices = STATUS_CHOICES,
			default = UNPAID,
			)
		datePosted = models.DateTimeField(auto_now =False, auto_now_add = True)
		paymentDate = models.DateField(null=True, blank = True)
		inCharge = models.CharField(max_length = 200)
		proof = models.FileField(null = True, blank = True)
		dueDate = models.DateField(null=True, blank = True)

		def __unicode__(self):
			return self.month +" "+self.billType
		class Meta:
			verbose_name_plural = "Bills"
			ordering = ("-paymentDate", "-status")