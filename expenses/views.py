from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import Income, Expense
from django.db.models import Sum
from .models import Expense,Income

from .forms import *

# Create your views here.
def Registerpage(request):
    if request.method=='POST':
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(loginpage)
    else:
        form=Registerform()
    return render(request,"register.html",{"form":form})


def user_logout(request):
    logout(request)
    return redirect('login')

    return redirect(loginpage)
def loginpage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request,"login.html")

def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    total_income = Income.objects.filter(
        user=request.user
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    total_expense = Expense.objects.filter(
        user=request.user
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    balance = total_income - total_expense

    recent_income = Income.objects.filter(
        user=request.user
    ).order_by('-date')[:5]

    recent_expense = Expense.objects.filter(
        user=request.user
    ).order_by('-date')[:5]

    return render(request, 'dashboard.html', {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'recent_income': recent_income,
        'recent_expense': recent_expense
    })



def add_income(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":

        source = request.POST.get('source')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        

        Income.objects.create(
            user=request.user,
            source=source,
            amount=amount,
            date=date,
            
        )

        return redirect('dashboard')

    return render(request, 'add_income.html')



def add_expense(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":

        Expensename = request.POST.get('Expensename')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        date = request.POST.get('date')
        description = request.POST.get('description')

        Expense.objects.create(
            user=request.user,
            Expensename=Expensename,
            category=category,
            amount=amount,
            date=date,
            description=description
        )

        return redirect('dashboard')

    return render(request, 'add_expense.html')


def transactions(request):

    if not request.user.is_authenticated:
        return redirect('login')

    incomes = Income.objects.filter(
        user=request.user
    ).order_by('-date')

    expenses = Expense.objects.filter(
        user=request.user
    ).order_by('-date')

    return render(request, 'transactions.html', {
        'incomes': incomes,
        'expenses': expenses
    })


def edit_income(request, id):

    if not request.user.is_authenticated:
        return redirect('login')

    income = Income.objects.get(
        id=id,
        user=request.user
    )

    if request.method == "POST":

        income.source = request.POST.get('source')
        income.amount = request.POST.get('amount')
        income.date = request.POST.get('date')
        
        income.save()

        return redirect('transactions')

    return render(request, 'edit_income.html', {
        'income': income
    })

def delete_income(request, id):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":

        income = Income.objects.get(
            id=id,
            user=request.user
        )

        income.delete()

    return redirect('transactions')



def edit_expense(request, id):

    if not request.user.is_authenticated:
        return redirect('login')

    expense = Expense.objects.get(
        id=id,
        user=request.user
    )

    if request.method == "POST":

        expense.Expensename = request.POST.get('Expensename')
        expense.category = request.POST.get('category')
        expense.amount = request.POST.get('amount')
        expense.date = request.POST.get('date')
        expense.description = request.POST.get('description')

        expense.save()

        return redirect('transactions')

    return render(request, 'edit_expense.html', {
        'expense': expense
    })


def delete_expense(request, id):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":

        expense = Expense.objects.get(
            id=id,
            user=request.user
        )

        expense.delete()

    return redirect('transactions')
