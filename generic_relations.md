"""
Generic Relations :

Introduction:
- generic relation in django enable one to many relationship with any object in model instances.
- it allows us to connect single model with multiple models.
- generic foriegn key works in a way such that we can randomize the behaviour of foriegn key.
- generic relation enable to retrieve the associated models which were connected by generic foriegn key.

Usage:
- ensure to include the 'django.contrib.contenttypes' in 'installed apps' in settings.py file
- use 'from django.contrib.contenttypes.models import ContentType' in models.py file, 'ContentType' stores information of models of the project.
- use 'from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation' to use generic foriegn key and generic relations in the project.

Generic Foriegn key:
- generic foriegn key is used to connect single model with multiple models.
- it enables randomizing the one to many relationship of a model instance.
- creating models with generic foriegn key includes 'content_type','object_id','content_object'
- 'content_type' defines the foriegn key usage, as the relation is established later, no need to specify the model.
- 'object_id' is a field to store the primary key values from the model instance relating to, uses PositiveIntegerField
- 'content_object' combines the 'content_type' and 'object_id' to retrieve the related object, here a db query is performed to get the instance of related model.

    "
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    "

- register the model in admin.py file to reflect in database
    admin.site.register(<model>)

Generic Relation:

- generic relation is used to retrieve the instance of model it is associated with.
  '
  abc=  GenericRelation('<related model>',content_type_field='content_type',object_id_field='object_id')
  '
  in models.py

- import GenericTabularInline in admin.py file to reflect in django admin.
    'from django.contrib.contenttypes.admin import GenericTabularInline'
        class Inline(GenericTabularInline):
        model = <related model>
        extra = 1

UseCase:
- a user wants to create 3 models author,genre,book
- the model book contains few instances which need to be linked with author and few instances which are needed to be linked to genre, the user also wants to findout which instances of model book are associated with author or genre
- in this case generic foriegn key and generic relations are used.
- declare the models for author,genre,book in models.py file as 

    models.py - 
    "
    from django.contrib.contenttypes.models import ContentType 
    from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation

    class Author(models.Model):
    name = models.CharField(max_length=255)
    books= GenericRelation('Book',content_type_field='content_type',object_id_field='object_id')

    def __str__(self):
        return self.name
    
    class Book(models.Model):
        title = models.CharField(max_length=255)
        content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
        object_id = models.PositiveIntegerField()
        content_object = GenericForeignKey('content_type', 'object_id')

        def __str__(self):
            return self.title
        
    class Genre(models.Model):
        name = models.CharField(max_length=255)
        books= GenericRelation('Book',content_type_field='content_type',object_id_field='object_id')

        def __str__(self):
            return self.name
    "

- register the models in admin.py file to reflect in django admin

    admin.py- 
    "
    from app.models import Author, Genre, Book

    class BookInline(GenericTabularInline):
        model= Book
        extra=1
    
    class AuthorAdmin(admin.ModelAdmin):
        inlines=[BookInline]    

    class GenreAdmin(admin.ModelAdmin):
        inlines=[BookInline]     
    
    admin.site.register(Author,AuthorAdmin)
    admin.site.register(Book)
    admin.site.register(Genre,GenreAdmin)
    "

- here we have implemented generic foriegn key and generic relation.
- now use 'py manage.py makemigrations' and 'py manage.py migrate' commands to write and execute queries for database.
- add a few instances in these models
- these are the outputs-

-using a generic foriegn key relation:
    ![genericforiegnkey](images/genericforiegnkey%20usage.png)
-here a content type is set as the author meaning that the book instance will be related to author model
- the object id is the set as the primary key of author instance which is connected to book instance.

- using a generic relation:
    ![genericrelation](images/generic%20relation%20usage.png)
here it retrieves the instances which are associated with itself.

"""

