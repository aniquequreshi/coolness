from django.urls import path, reverse_lazy
from . import views  # for function based views


from matrimonial.views import PersonCreateView, PersonUpdateView, PersonDetailView, PersonListView, EditPersonRedirectView

urlpatterns = [
    path('', views.index_view, name='index'),
    path('create/', PersonCreateView.as_view(), name ='person-create'),
    path('update/<int:pk>/', PersonUpdateView.as_view(), name ='person-update'),
    path('detail/<int:pk>/', PersonDetailView.as_view(), name ='person-detail'),
    path('list/', PersonListView.as_view(), name='person-list'),
    path('secure/', views.home_view, name='secure-home'),
    path('edit/', EditPersonRedirectView.as_view(url=reverse_lazy('person-update')), name='person-edit-create'),

]
