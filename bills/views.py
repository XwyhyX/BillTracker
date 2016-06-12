from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Bills
from .forms import AddForm

# Create your views here.
def index(request):
	form = AddForm(request.POST or None, request.FILES or None)
	object_list = Bills.objects.all()
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('')
		context = {"object_list":object_list,"message":"BILL ADDED"}
	context = {"object_list":object_list,"form":form}
	return render(request, 'bills/index.html',context)

def pay(request, filterString = ""):
	object_list = Bills.objects.all().filter(status="NP")
	filter_month = Bills.objects.all().filter(month = filterString, status="NP")
	context = {"object_list":object_list,"filter_month":filter_month}
	return render(request, 'bills/pay.html',context)
def history(request, filterString = ""):
	object_list = Bills.objects.all()
	filter_month = Bills.objects.all().filter(month = filterString)
	context = {"object_list":object_list,"filter_month":filter_month}
	return render(request, 'bills/history.html',context)
def details(request, bill_id):
	object_list = Bills.objects.all().filter(id = bill_id)
	context = {"object_list":object_list}
	return render(request, 'bills/details.html',context)
