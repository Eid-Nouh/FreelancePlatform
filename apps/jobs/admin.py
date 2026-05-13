from django.contrib import admin
from .models import Job, Application


# =========================
# Job Admin
# =========================
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'budget', 'user', 'created_at')
    search_fields = ('title', 'company')
    list_filter = ('company', 'created_at')


# =========================
# Application Admin
# =========================
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'job', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('job',)


# =========================
# Register Models
# =========================
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)