from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from event_reporting.forms import EventCreateForm
from django.core.paginator import Paginator
from .models import Customer, Event


def isAdmin(user):
    return user.is_superuser

#@user_passes_test(isAdmin)
def create_event(request):
    if request.method == "POST":
        form = EventCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = EventCreateForm()
    return render(request, "events/event_create.html", {"form":form})

#@user_passes_test(isAdmin)
def delete_event(request, id):
    event_delete = get_object_or_404(Event, pk=id)
    if request.method=="POST":
        event_delete.delete()
        return redirect("event_list")
    else:
         return render(request, "events/event_delete.html", {"event":event_delete})

#@user_passes_test(isAdmin)
def list_event(request):
    events = Event.objects.all().order_by('date')
    paginator = Paginator(events, 3)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'events/event_list.html', {
        'page_obj': page_obj,   
    })

#@user_passes_test(isAdmin)
def edit_event(request, id):
    event_edit = get_object_or_404(Event, pk=id)
    if request.method == "POST":
        form = EventCreateForm(request.POST, request.FILES, instance=event_edit)
        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = EventCreateForm(instance=event_edit)
    
    return render(request, "events/event_edit.html", {"form":form})

def getEventsByCustomer(request, name):
    events = Event.objects.filter(customer__name=name).order_by("date")
    customer = Customer.objects.all()

    paginator = Paginator(events, 3)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'events/event_list.html', {
        'customer': customer, 
        'page_obj': page_obj,
        'choosenCustomer': name,
    })
