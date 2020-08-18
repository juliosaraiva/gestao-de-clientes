from django.urls import path
from .views import home, getLogout, MyView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', home, name='home'),
    path('logout/', getLogout, name='logout'),
    path("home2/", TemplateView.as_view()),
    path("myview/", MyView.as_view()),
]