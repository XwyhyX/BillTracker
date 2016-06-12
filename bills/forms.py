from django import forms
from .models import Bills

class AddForm(forms.ModelForm):
	class Meta:
		model = Bills
		fields = ["month","billType","amountDue","status","paymentDate","inCharge","proof","dueDate"]