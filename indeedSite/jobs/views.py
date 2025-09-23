from django.shortcuts import render, redirect, get_object_or_404
from .models import Job


# Create your views here.
def index(request):
    return render(request, 'jobs/index.html', {'template_data': {}})

def show(request, id):
    job = Job.objects.get(id=id)
    template_data = {}
    template_data['title'] = job.name
    return render(request, 'jobs/show.html', {'template_data': template_data})
