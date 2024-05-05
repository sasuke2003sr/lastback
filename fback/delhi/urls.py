from django.urls import path
from . import views

urlpatterns = [
    # path('delhi/', views.delhi, name='delhi'),
    path('', views.delhi, name='delhi'),
    path('tender.html', views.tender_view, name='tender'),
    path('login.html', views.login_view, name='login'),
    # path('delhi/contact/<int:id>', views.contact, name='contact'),
]