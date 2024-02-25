from django.contrib import admin
from .models import Book, BookContributor, Contributor, Review, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn']
    list_filter = ['publisher', 'publication_date']
    date_hierarchy = 'publication_date'
    search_fields = ['title', 'isbn', 'publisher__name']


class ReviewAdmin(admin.ModelAdmin):
    exclude = ['date_edited']


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ['first_names', 'last_names']
    list_filter = ['last_names']
    search_fields = ['first_names', 'last_names__startswith']
    fieldsets = [
        ('Personal', {'fields': ('first_names', 'last_names')}),
        ('Social', {'fields': ('email',)})
    ]


# Register your models here.
admin.site.register(BookContributor)
# admin.site.register(Contributor)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Publisher)
