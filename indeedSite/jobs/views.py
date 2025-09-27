from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Job


# Create your views here.
def index(request):
    return render(request, 'jobs/index.html', {'template_data': {}})

def show(request, id):
    job = Job.objects.get(id=id)
    template_data = {}
    template_data['title'] = job.name
    return render(request, 'jobs/show.html', {'template_data': template_data})

def profile(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    template_data = {
        "profile_user": profile_user
    }
    return render(request, "jobs/profile.html", {
        "template_data": template_data
    })
