from django.contrib import admin

<<<<<<< HEAD
from .models import Author, Book, Address, Country
=======
<<<<<<< HEAD
<<<<<<< ours
from .models import Author, Book, Address, Country
=======
from .models import Book
>>>>>>> theirs
=======
from .models import Author, Book, Address, Country
>>>>>>> b44c8c5 (New relationships)
>>>>>>> 4effc7d (New relationships)

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = (
        "author",
        "rating",
    )
    list_display = (
        "title",
        "author",
    )


admin.site.register(Book, BookAdmin)
<<<<<<< HEAD
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
=======
<<<<<<< HEAD
<<<<<<< ours
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
=======
>>>>>>> theirs
=======
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
>>>>>>> b44c8c5 (New relationships)
>>>>>>> 4effc7d (New relationships)
