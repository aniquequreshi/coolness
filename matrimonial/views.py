from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# import copy

from matrimonial.models import Person
from matrimonial.forms import PersonForm


# Create your views here.
def index_view(request):
    return render(request, 'matrimonial/index.html')


@login_required
def home_view(request):  # Secure Home
    return render(request, 'matrimonial/secure_home.html')


class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm

    # success_url = reverse_lazy('person-detail')

    def form_valid(self, form):
        form.instance.the_user = self.request.user
        # form.instance.the_user.save()
        return super(PersonCreateView, self).form_valid(form)


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm
    # queryset = Person.objects.filter()

    # success_url = reverse_lazy('person-detail')
    # def get_object(self, queryset=None):
    #     # get the existing object or created a new one
    #     obj, created = Person.objects.get_or_create(col_1=self.kwargs['value_1'], col_2=self.kwargs['value_2'])
    #
    #     return obj


class PersonDetailView(LoginRequiredMixin, DetailView):
    # model = Person
    context_object_name = 'person'
    # success_url = reverse_lazy('person-detail')

    queryset = Person.objects.all()

    def get_object(self):
        privacy = 'PRIVATE'
        display = "Not Provided"
        obj = super().get_object()
        if (obj.first_name_answer == privacy):
            obj.first_name = display
        if obj.last_name_answer == privacy:
            obj.last_name = display
        # obj.save()  DON'T WANT TO SAVE IT
        return obj


class PersonListView(LoginRequiredMixin, ListView):
    model = Person
    context_object_name = 'person_detail'

# This will Create or Update
class EditPersonRedirectView(generic.RedirectView):
    def get_redirect_url(self):
        z = self.request.user.pk #logged in User primary key
        y = 0
        try:
            y = Person.objects.get(the_user=z).pk  #Primary key of previously created Person Object
        except:
            y = 0
        if y==0: # No person was previously created
        # if Person.objects.get(the_user=self.request.user.id).DoesNotExis:
            return reverse('person-create')
        else:
            return reverse('person-update', args=[y])
