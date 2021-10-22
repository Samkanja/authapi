from django.urls import path
from .views import LogoutView, Registration, Loginview, UserView

urlpatterns = [
    path('register/', Registration.as_view()),
    path('login/', Loginview.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view())
   
]
