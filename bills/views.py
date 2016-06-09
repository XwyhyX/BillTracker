from django.shortcuts import render
from .models import Bills

# Create your views here.
def index(request):
	object_list = Bills.objects.all()
	context = {"object_list":object_list}
	print object_list
	return render(request, 'bills/index.html',context)
def pay(request):
	object_list = Bills.objects.all().filter(status="UD")
	context = {"object_list":object_list}
	print object_list
	return render(request, 'bills/pay.html',context)
def history(request):
	object_list = Bills.objects.all()
	context = {"object_list":object_list}
	return render(request, 'bills/history.html',context)
def details(request, bill_id):
	object_list = Bills.objects.all().filter(id = bill_id)
	context = {"object_list":object_list}
	return render(request, 'bills/details.html',context)