from django import forms
from .models import Expense, Goal

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category','description', 'amount', 'date']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ExpenseForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ExpenseForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'current_amount', 'deadline']

