from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pets_list, name='pets-list'),
    path('pets/<int:pet_id>/', views.detail, name='detail')

    # path('w/<str:slug>/', ArticleDetailView.as_view(), name='wiki-details-page'),
    # path('create/', ArticleCreateView.as_view(), name='create'),
]
