from django.urls import path
from . import views

urlpatterns = [
    # path('delhi/', views.delhi, name='delhi'),
    path('', views.delhi, name='delhi'),
    # path('delhi/contact/<int:id>', views.contact, name='contact'),
]