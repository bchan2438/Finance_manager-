from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .models import Expense, Goal
from .forms import ExpenseForm, GoalForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'expenses/index.html')
@login_required
def goals_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'expenses/goals_list.html', {'goals': goals})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goals_list')
    else:
        form = GoalForm()
    return render(request, 'expenses/add_goal.html', {'form': form})

@login_required
def edit_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goals_list')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'expenses/edit_goal.html', {'form': form})
@login_required
def delete_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id, user=request.user)
    if request.method == 'POST':
        goal.delete()
        return redirect('goals_list')
    else:
        return render(request, 'expenses/delete_goal.html', {'goal': goal})


@login_required
def expenses_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expenses/expenses_list.html', {'expenses': expenses})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expenses_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'expenses/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'expenses/logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'expenses/register.html', {'form': form})

