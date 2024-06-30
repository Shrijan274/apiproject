from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Define a custom UserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your CustomUser model with the custom UserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
