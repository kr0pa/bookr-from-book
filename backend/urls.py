from django.contrib import admin
from django.urls import path
import app_reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_reviews.views.index),
    path('book-search/', app_reviews.views.book_search),
]
