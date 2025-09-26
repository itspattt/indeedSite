from django.shortcuts import render

# Create your views here.
def index(request):
    template_data = {}
    return render(request, "accounts/profile.html", {'template_data': template_data})
