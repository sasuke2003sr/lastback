# views.py

# from django.shortcuts import render
# from .models import Delhi


from django.http import HttpResponse
from django.template import loader

def delhi(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

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
