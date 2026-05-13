from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    model = CustomUser

    # اللي يظهر في الجدول
    list_display = (
        'username',
        'email',
        'phone_number',
        'user_type',
        'is_staff',
        'is_active'
    )

    # البحث
    search_fields = (
        'username',
        'email',
        'phone_number'
    )

    # فلترة
    list_filter = (
        'user_type',
        'is_staff',
        'is_active'
    )

    # تعديل الفورم في admin
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {
            'fields': ('phone_number', 'user_type')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {
            'fields': ('phone_number', 'user_type')
        }),
    )


# تسجيل الموديل
admin.site.register(CustomUser, CustomUserAdmin)