from django.contrib import admin
from .models import Job, Application

# Register your models here.
admin.site.register(Job)

# @admin.register(Job)
# class JobAdmin(admin.ModelAdmin):
#     list_display = ("title", "company", "location", "salary_min", "salary_max")

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "user", "status", "applied_at")
    list_filter = ("status", "applied_at")
    search_fields = ("job__title", "user__username")