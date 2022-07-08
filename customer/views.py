from django.shortcuts import redirect, render
from customer.forms import CustomerForm

from customer.models import Customer

# Create your views here.
def index(request):
    customer = Customer.objects.all()
    return render(request, 'customer/index.html',{'customers':customer})

def create(request):
    return render(request, 'customer/create.html')

def saveFn(request):
    print(request.FILES)
    # print(request.method)
    # print(request.POST)
    data = CustomerForm(request.POST, request.FILES) #mapping with form
    # print(data)
    data.save()
    # return render(request, 'customer/create.html')
    return redirect('/customer')

def edit(request, id):
    print(id)

    data = Customer.objects.get(id=id)
    return render(request, 'customer/edit.html', {'data':data})

def update(request,id):
    data = Customer.objects.get(id=id)
    form = CustomerForm(request.POST, instance=data)
    form.save()

    return redirect('/customer')

def delete(request,id):
    data = Customer.objects.get(id=id)
    data.delete()
    return redirect('/customer')


