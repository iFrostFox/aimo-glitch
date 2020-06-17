from django.contrib import admin
from .models import Newspaper
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class NewspaperAdmin(admin.ModelAdmin):
    fields = ["title",
              "authors",
              "date_published",
              "content",
              "slug"]
              
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Newspaper, NewspaperAdmin)
