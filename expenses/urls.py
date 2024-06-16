from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='expenses/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('index/', views.index, name='index'),
    path('expenses/', views.expenses_list, name='expenses_list'),
    path('goals/', views.goals_list, name='goals_list'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('add_goal/', views.add_goal, name='add_goal'),
    path('goals/edit/<int:goal_id>/', views.edit_goal, name='edit_goal'),
    path('goals/delete/<int:goal_id>/', views.delete_goal, name='delete_goal'),


]
