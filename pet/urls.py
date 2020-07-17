from django.urls import path
from . import views
from pet.views import PetsList, PetDetail, HomePage, AppointmentList

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    # path('pets/', views.pets_list, name='pets-list'),
    path('pets/<int:pet_id>/', PetDetail.as_view(), name='detail'),
    path('pets/', PetsList.as_view(), name='pets-list'),
    path('appointments/', AppointmentList.as_view(), name='appointment-list')
    # path('w/<str:slug>/', ArticleDetailView.as_view(), name='wiki-details-page'),
    # path('create/', ArticleCreateView.as_view(), name='create'),
]
