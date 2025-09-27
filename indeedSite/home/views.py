from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    template_data = {}
    template_data["users"] = users
    return render(request, 'home/index.html', {"template_data": template_data})