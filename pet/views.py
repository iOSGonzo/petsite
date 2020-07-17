from django.shortcuts import render
from .models import Pet, Appointment
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from pet.forms import PetForm, AppointmentForm
from pet.models import Pet, Appointment

class PetsList(ListView):
  def get(self, request, *args, **kwargs):
      context = {'form': PetForm(), 'pets': Pet.objects.all()}
      return render(request, 'pets-list.html', context)

  def post(self, request, *args, **kwargs):
    form = PetForm(request.POST)
    if form.is_valid():
        article = form.save()
        return HttpResponseRedirect(reverse_lazy('home'))
    return render(request, 'pets-list.html', {'form': form})

class AppointmentList(ListView):
  def get(self, request, *args, **kwargs):
      context = {
            'appointments': Appointment.objects.order_by('date_of_appointment'),
            'form': AppointmentForm()
      }
      return render(request, 'calendar.html', context)

  def post(self, request, *args, **kwargs):
    form = AppointmentForm(request.POST)
    if form.is_valid():
        article = form.save()
        return HttpResponseRedirect(reverse_lazy('home'))
    return render(request, 'calendar.html', {'form': form})


class HomePage(CreateView):
    def get(self, request):
        """ GET a list of Articles. """
        return render(request, 'home.html')

class PetDetail(DetailView):

  def get(self, request, pet_id):
      context = {'pet': Pet.objects.get(id=pet_id)}
      return render(request, 'detail.html', context)

  # def post(self, request, *args, **kwargs):
  #   form = PetForm(request.POST)
  #   if form.is_valid():
  #       article = form.save()
  #       return HttpResponseRedirect(reverse_lazy('home'))
  #   return render(request, 'pets-list.html', {'form': form})
