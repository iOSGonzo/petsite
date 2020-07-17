from django.urls import path, include
from accounts.views import SignupView, LoginView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    # path('logout/', LoginView.as_view(), name='login'),
    # path('login/', LoginView.as_view(), name='login'),
]
