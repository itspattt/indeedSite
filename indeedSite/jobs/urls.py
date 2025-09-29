from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("<int:id>/", views.job_detail, name="job_detail"),
    path("<int:id>/apply/", views.apply_to_job, name="apply_to_job"),
    path("map/", views.job_map, name="job_map"),
    path("applications/", views.my_applications, name="my_applications"),
    path('recommended/', views.recommended_jobs, name='recommended_jobs'),
    path('map-view/', views.job_map, name='job_map'),
]