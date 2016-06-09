from django.contrib import admin
from .models import Bills
# Register your models here.
class BillModelAdmin(admin.ModelAdmin):
	list_display = ["month","billType","amountDue", "datePosted"]
	list_filter = ["status"]

	search_fields = ["month","inCharge","billType","status"]

	class Meta:
		model = Bills

admin.site.register(Bills, BillModelAdmin)