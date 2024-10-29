from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Barber, BarberShop, Customer
from django.shortcuts import render

# Create your views here.
class BarberListView(ListView):
    model = Barber
    template_name = 'blist.html'
    context_object_name = 'all_b_list'

class BarberDetailView(DetailView):
    model = Barber
    template_name = 'b_detail.html'

class BarberCreateView(CreateView):
    model = Barber
    template_name = 'b_create.html'
    fields = ['name', 'num_customers', 'b_shop']

class BarberUpdateView(UpdateView):
    model = Barber
    template_name = 'b_edit.html'
    fields = ['num_customers']

class CBListView(ListView):
    model = Customer
    template_name = 'cb_list.html'
    context_object_name = 'all_c_list'

def query1(request):
    # Initialize an empty context to pass to the template
    context = {
        'customers': None,
        'error_message': None,
    }

    try:
        customers = Customer.objects.order_by('-name')
        context['customers'] = customers

    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query1.html', context)


def query2(request):
    # Initialize an empty context to pass to the template
    context = {
        'customer_count': None,
        'barber_name':None,
        'error_message': None,
    }

    try:
        barber_match = Barber.objects.get(name="James Miller")
        context['customer_count'] = Customer.objects.filter(barber=barber_match).count()
        context['barber_name'] = barber_match.name
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    return render(request, 'db_query2.html', context)


