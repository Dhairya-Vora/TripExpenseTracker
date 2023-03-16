from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import expense
import time
# Create your views here.
def home(request):

    if request.method == 'POST':
        dict = {}
        for key,value in request.POST.items():
            dict[key] = value
        name = dict['name']
        type = dict['type']
        remarks = dict['remarks']
        amount = dict['amount']
        saveData = expense(name=name,type=type,remarks=remarks,amount=amount)
        saveData.save()
        print(dict)
    #


    return render(request,'home.html')

def expense_list(request):
    expenses = expense.objects.all().order_by('time')
    print(expenses)
    return render(request, 'show_expense.html', {'expenses': expenses})

def expense_delete(request, expense_id):
    exp = get_object_or_404(expense, id=expense_id)
    if request.method == 'POST':
        exp.delete()
        return redirect('expense_list')
    return render(request, 'expense_delete.html', {'expense': exp})#