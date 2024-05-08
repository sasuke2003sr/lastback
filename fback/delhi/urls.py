from django.urls import path
from . import views

urlpatterns = [
    # path('delhi/', views.delhi, name='delhi'),
    path('index.html', views.delhi, name='delhi'),
    path('contact.html', views.contact_view, name='contact'),
    path('gallery.html', views.gallery_view, name='gallery'),
    path('tender.html', views.tender_view, name='tender'),
    path('login.html', views.login_view, name='login'),
    path('master.html',views.master_view,name='master')
    # path('delhi/contact/<int:id>', views.contact, name='contact'),
]