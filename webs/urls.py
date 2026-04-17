from django.urls import path
from .views import show,postdetail
urlpatterns = [
    path('',show,name='home'),
    path('<int:pk>/',postdetail.as_view(),name='detail'),
]

