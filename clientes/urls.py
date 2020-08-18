from django.urls import path
from .views import (
    persons_list, persons_new, persons_update,
    persons_delete, PersonList, PersonDetail,
    PersonCreate,
)

urlpatterns = [
    path('list/', persons_list, name='persons_list'),
    path('new/', persons_new, name='persons_new'),
    path('update/<int:id>/', persons_update, name='persons_update'),
    path('delete/<int:id>/', persons_delete, name='persons_delete'),
    path('person_list/', PersonList.as_view(), name='person-list'),
    path('person_detail/<int:pk>', PersonDetail.as_view(), name='person-detail'),
    path('person_create/', PersonCreate.as_view(), name='person-create')
]