from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Job, Application
from django.shortcuts import render
from django.http import JsonResponse

# 1. Job Listings + Search/Filters
def job_list(request):
    jobs = Job.objects.all()

    # --- filters ---
    title = request.GET.get("title")
    skills = request.GET.get("skills")
    location = request.GET.get("location")
    remote = request.GET.get("remote")
    visa = request.GET.get("visa")
    salary_min = request.GET.get("salary_min")
    salary_max = request.GET.get("salary_max")

    if title:
        jobs = jobs.filter(title__icontains=title)
    if skills:
        jobs = jobs.filter(skills_required__icontains=skills)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if remote:  # e.g., ?remote=1
        jobs = jobs.filter(remote=True)
    if visa:  # e.g., ?visa=1
        jobs = jobs.filter(visa_sponsorship=True)
    if salary_min:
        jobs = jobs.filter(salary_min__gte=salary_min)
    if salary_max:
        jobs = jobs.filter(salary_max__lte=salary_max)

    return render(request, "jobs/job_list.html", {"jobs": jobs})


# 2. Job Detail Page
def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, "jobs/job_detail.html", {"job": job})


# 3. Apply to a Job
# @login_required
def apply_to_job(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == "POST":
        note = request.POST.get("note", "")
        Application.objects.create(user=request.user, job=job, note=note, status="Applied")
        return redirect("job_detail", id=job.id)

    return render(request, "jobs/apply.html", {"job": job})


# 4. Job Map (JSON endpoint for Leaflet/Google Maps)
def job_map(request):
    jobs = Job.objects.values("id", "title", "company", "location")
    return JsonResponse(list(jobs), safe=False)

# @login_required
def my_applications(request):
    # Get all applications for the logged-in user
    applications = Application.objects.filter(user=request.user).order_by('-applied_at')
    return render(request, "jobs/my_applications.html", {"applications": applications})

# @login_required
def recommended_jobs(request):
    user_skills = request.user.profile.skills.split(",")  # assuming comma-separated skills
    jobs = Job.objects.none()
    for skill in user_skills:
        jobs |= Job.objects.filter(skills_required__icontains=skill.strip())
    jobs = jobs.distinct()
    return render(request, "jobs/recommended_jobs.html", {"jobs": jobs})

def job_map(request):
    jobs = Job.objects.values("id", "title", "company", "location")  # location must be lat,lng
    return JsonResponse(list(jobs), safe=False)