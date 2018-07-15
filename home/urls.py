from django.urls import path
from .views import home, getLogout

urlpatterns = [
    path('', home, name='home'),
    path('logout/', getLogout, name='logout')
]