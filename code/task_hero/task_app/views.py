from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.utils.timezone import now
from .models import Task, StatusChoices, PriorityChoices
from .forms import TaskForm
from datetime import datetime


def home(request):
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        greeting = "Good Morning!"
        time_of_day = 'morning' 
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon!"
        time_of_day = 'day'
    elif 18 <= current_hour < 22:
        greeting = "Good Evening!"
        time_of_day = 'night'   
    else:
        greeting = "Good Night!"
        time_of_day = 'Late night'

    context = {
        'time_of_day':time_of_day,
        'greeting': greeting
    }
    return render(request, "task-app/home.html", context)

@login_required
def dashboard(request):
    tasks = Task.objects.filter(username=request.user)
    
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        greeting = "Good Morning!"
        time_of_day = 'morning' 
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon!"
        time_of_day = 'day'
    elif 18 <= current_hour < 22:
        greeting = "Good Evening!"
        time_of_day = 'night'   
    else:
        greeting = "Good Night!"
        time_of_day = 'Late night'  
   

    upcoming_tasks = tasks.filter(due_date__gte=timezone.now(), due_date__lte=timezone.now() + timedelta(days=7)).order_by('due_date')

    tasks_by_status = {
        'to_do': tasks.filter(status='to_do').count(),
        'in_progress': tasks.filter(status='in_progress').count(),
        'completed': tasks.filter(status='completed').count(),

    }

    tasks_todo = {
        'to_do': tasks.filter(status='to_do'),
        'in_progress' : tasks.filter(status='in_progress'),
        'complete' : tasks.filter(status='complete'),
    }
    return render(request, 'task-app/dashboard.html', {
        'tasks': tasks,
        'upcoming_tasks': upcoming_tasks,
        'tasks_by_status': tasks_by_status,
        'time_of_day':time_of_day,
        'greeting': greeting,
        'tasks_todo': tasks_todo
    })


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        greeting = "Good Morning!"
        time_of_day = 'morning' 
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon!"
        time_of_day = 'day'  
    
    elif 18 <= current_hour < 22:
        greeting = "Good Evening!"
        time_of_day = 'night'

    else:
        greeting = "Good Night!"
        time_of_day = 'Late night'


    if request.user != task.username:
        messages.error(request, "You do not have permission to view that task, try logging in with different details.")
        return redirect("task_app:home")
    context = {
        "task":task,
        "greeting":greeting,
        "time_of_day": time_of_day
    }
    return render(request, 'task-app/task-detail.html', context)



@login_required
def add_task(request):
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        greeting = "Good Morning!"
        time_of_day = 'morning' 
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon!"
        time_of_day = 'day'  
    elif 18 <= current_hour < 22:
        greeting = "Good Evening!"
        time_of_day = 'night'
    else:
        greeting = "Good Night!"
        time_of_day = 'Late night' 

    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.username = request.user 
            task.save() 
            messages.success(request, "Task added successfully!")
            return redirect("task_app:dashboard")  # Redirect to the dashboard view
    return render(request, "task-app/add-task.html", {"form": form, "greeting":greeting, "time_of_day":time_of_day})

  
@login_required 
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        greeting = "Good Morning!"
        time_of_day = 'morning' 
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon!"
        time_of_day = 'day' 
    elif 18 <= current_hour < 22:
        greeting = "Good Evening!"
        time_of_day = 'day'  
    else:
        greeting = "Good Night!"
        time_of_day = 'Late night' 
    status_choices = StatusChoices
    priority_choices = PriorityChoices

    if task.username != request.user:
        messages.error(request, "You do not have permission to edit this task.")
        return redirect("task_app:dashboard")
   
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            print("Form is valid")
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect("task_app:dashboard")
        else:
            print("Form is invalid")
            print(form.errors)
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            # messages.error(request, "There were errors in the form. Please correct them.")

    else:
        form = TaskForm(instance=task)
    context = {
        'form': form,
        'task': task,
        'status_choices': status_choices,
        'priority_choices': priority_choices,
        'greeting':greeting,
        'time_of_day':time_of_day
    }

    return render(request, 'task-app/update-task.html', context)
       
@login_required
def confirm_delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, username=request.user)
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        greeting = "Good Morning!"
        time_of_day = 'morning' 
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon!"
        time_of_day = 'day' 
    elif 18 <= current_hour < 22:
        greeting = "Good Evening!"
        time_of_day = 'day'  
    else:
        greeting = "Good Night!"
        time_of_day = 'Late night'  
    if request.user != task.username:
        messages.error(request, "You do not have permission to delete that Task")
        return redirect("task_app/home")
    return render(request, 'task-app/confirm-delete-task.html', {'task': task, 'greeting':greeting, 'time_of_day':time_of_day})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, username=request.user)
    if request.user != task.username:
        messages.error(request, "you do not have permission to delete that task")
        return redirect("task_app:home")
    if request.method =="POST":
        task.delete()
        messages.success(request, "Task deleted successfully")
    return redirect("task_app:dashboard")


