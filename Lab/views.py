from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic.base import View, TemplateView
from .models import Customer, Plane, Ticket


class CustomersClassTable(View):
    def get(self, request, *args, **kwargs):
        return render(request, "customers.html", {"customers": Customer.objects.all()} )


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, "index.html", {"num_visits":num_visits})


def customers_table(request):
    customers = Customer.objects.all()
    return render(request, "customers.html", {"customers": customers})


def planes_table(request):
    planes = Plane.objects.all()
    return render(request, "planes.html", {"planes": planes})


def tickets_table(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets.html", {"tickets": tickets})


def create_customer(request):
    if request.method == "POST":
        customer = Customer()
        customer.name = request.POST.get("name")
        customer.phone = request.POST.get("phone")
        customer.save()
    return HttpResponseRedirect("/customers/")


def create_plane(request):
    if request.method == "POST":
        plane = Plane()
        plane.city_from = request.POST.get("city_from")
        plane.city_to = request.POST.get("city_to")
        plane.departure_date = request.POST.get("departure_date")
        plane.departure_time = request.POST.get("departure_time")
        plane.landing_date = request.POST.get("landing_date")
        plane.landing_time = request.POST.get("landing_time")
        plane.save()
    return HttpResponseRedirect("/planes/")


def create_ticket(request):
    if request.method == "POST":
        ticket = Ticket()
        ticket.customer = Customer.objects.get(id=request.POST.get("customer"))
        ticket.plane = Plane.objects.get(id=request.POST.get("plane"))
        ticket.price = request.POST.get("price")
        ticket.save()
    return HttpResponseRedirect("/tickets/")


def edit_customer(request, id):
    try:
        customer = Customer.objects.get(id=id)

        if request.method == "POST":
            customer.name = request.POST.get("name")
            customer.phone = request.POST.get("phone")
            customer.save()
            return HttpResponseRedirect("/customers/")
        else:
            return render(request, "edit_customer.html", {"customer": customer})
    except Customer.DoesNotExist:
        return HttpResponseNotFound("<h2>Customer not found</h2>")


def edit_plane(request, id):
    try:
        plane = Plane.objects.get(id=id)

        if request.method == "POST":
            plane.city_from = request.POST.get("city_from")
            plane.city_to = request.POST.get("city_to")
            plane.departure_date = request.POST.get("departure_date")
            plane.departure_time = request.POST.get("departure_time")
            plane.landing_date = request.POST.get("landing_date")
            plane.landing_time = request.POST.get("landing_time")
            plane.save()
            return HttpResponseRedirect("/planes/")
        else:
            return render(request, "edit_plane.html", {"plane": plane})
    except Plane.DoesNotExist:
        return HttpResponseNotFound("<h2>Plane not found</h2>")


def edit_ticket(request, id):
    try:
        ticket = Ticket.objects.get(id=id)

        if request.method=="POST":
            ticket.customer = Customer.objects.get(id=request.POST.get("customer"))
            ticket.plane = Plane.objects.get(id=request.POST.get("plane"))
            ticket.price = request.POST.get("price")
            ticket.save()
            return HttpResponseRedirect("/tickets/")
        else:
            return render(request, "edit_ticket.html", {"ticket": ticket})
    except Ticket.DoesNotExist:
        return HttpResponseNotFound("<h2>Ticket not found</h2>")


def delete_customer(request, id):
    try:
        customer = Customer.objects.get(id=id)
        customer.delete()
        return HttpResponseRedirect("/customers/")
    except Customer.DoesNotExist:
        return HttpResponseNotFound("<h2>Customer not found</h2>")


def delete_plane(request, id):
    try:
        plane = Plane.objects.get(id=id)
        plane.delete()
        return HttpResponseRedirect("/planes/")
    except Plane.DoesNotExist:
        return HttpResponseNotFound("<h2>Plane not found</h2>")


def delete_ticket(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        ticket.delete()
        return HttpResponseRedirect("/tickets/")
    except Ticket.DoesNotExist:
        return HttpResponseNotFound("<h2>Ticket not found</h2>")