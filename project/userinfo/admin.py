from django.contrib import admin
from userinfo.models import UserInfo,TokenVerification
from django.contrib.auth.admin import UserAdmin

class CustomuserInfo(admin.ModelAdmin):
    model=UserInfo
    list_display=('name','email','age','gender','address' ,'is_staff','is_active', 'is_superuser')
    search_fields = ('email', 'name')
    list_filter = ('gender','is_staff', 'is_superuser', 'is_active',)
    ordering = ('name',)
   
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'age', 'gender', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        
    )
    readonly_fields = ('password',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

admin.site.register(UserInfo,CustomuserInfo)
admin.site.register(TokenVerification)
