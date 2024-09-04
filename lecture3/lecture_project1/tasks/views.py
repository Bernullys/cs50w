from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect


tasks = []
# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    return render (request, "tasks/index.html", {
        "tasks": tasks
    })

# Add a new task:
def add(request):

    # Check if method is POST:
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)
        # Check if form data is valid (server-side)
        if form.is_valid():
            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]
            # Add the new task to our list of tasks
            tasks.append(task)
            # Redirect user to list of tasks
            # In order to redirect the user after a successful submission, we need to import: reverse and HttpResponseRedirect
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # Here we passing the form so the user can see whay is not valid:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })