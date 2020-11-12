from django.contrib import admin
from jobs.models import Job
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    exclude = ("creater", "create_date", "modified_date")
    list_display = ("job_name", "job_type", "job_city", "creater", "create_date", "modified_date")

    def save_model(self, request, obj, form, change):
        obj.creater = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Job, JobAdmin)