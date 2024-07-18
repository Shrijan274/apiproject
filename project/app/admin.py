from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import CustomUser,Author, Genre, Book
from django.contrib.contenttypes.admin import GenericTabularInline


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class BookInline(GenericTabularInline):
    model= Book
    extra=1

class BookAdmin(admin.ModelAdmin):
    model= Book
    list_display=('title','object_id','content_object')

class AuthorAdmin(admin.ModelAdmin):
    model=Author
    list_display=('name','id')
    inlines=[BookInline]    

class GenreAdmin(admin.ModelAdmin):
    model=Genre
    list_display=('name','id')
    inlines=[BookInline] 


#registering the customuser model with custom user admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Genre,GenreAdmin)
