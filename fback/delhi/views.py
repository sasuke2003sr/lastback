# views.py

# from django.shortcuts import render
# from .models import Delhi


from django.http import HttpResponse
from django.template import loader
from .models import Tender
from .models import *

def delhi(request):
  return render(request,"index.html")

from django.shortcuts import render

def tender_view(request):
    # Add your view logic here
    return render(request, 'tender.html')  # Assuming tender.html is in your templates directory


def gallery_view(request):
    # Add your view logic for the gallery page here
    return render(request, 'gallery.html')


def contact_view(request):
    # Add your view logic for the gallery page here
    return render(request, 'contact.html')


def tender_list(request):
    tenders = Tender.objects.all()
    return render(request, 'tender_list.html', {'tenders': tenders})
def login_view(request):
    # Add your view logic for login page here
    if request.method == "POST":
        data=request.POST
        Name=data.get("Name")
        Password=data.get("Password")
        TenderId=data.get("TenderId")
        Title=data.get("Title")
        Date=data.get("Date")
        Deadline=data.get("Deadline")

        Login.objects.create(
            Name=Name,
            Password=Password,
            TenderId=TenderId,
            Title=Title,
            Date=Date,
            Deadline=Deadline,
        )
    return render(request, 'login.html')
# def index(request):
#     # Add any context data needed for index.html
#     context = {
#         # Add context data here if needed
#     }
#     return render(request, 'index.html', context)

# def delhi(request):
#     mydelhi = Delhi.objects.all().values()
#     context = {
#         'mydelhi': mydelhi,
#     }
#     return render(request, 'all_delhi.html', context)

# def contact(request, id):
#     mydelhi = Delhi.objects.get(id=id)
#     context = {
#         'mydelhi': mydelhi,
#     }
#     return render(request, 'contact.html', context)

def master_view(request):
    return render(request,"master.html")