from django.contrib import admin
from .models import Service


# =========================
# Service Admin
# =========================
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'idea_name',
        'service_type',
        'expected_price',
        'full_name',
        'phone',
        'email'
    )

    search_fields = (
        'idea_name',
        'service_type',
        'full_name',
        'email',
        'phone'
    )

    list_filter = (
        'service_type',
    )


# =========================
# Register
# =========================
admin.site.register(Service, ServiceAdmin)