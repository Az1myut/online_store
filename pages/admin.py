from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
=======
from .models import BbCodeModel
# Register your models here.

class BbCodeModelAdmin(admin.ModelAdmin):
    list_display = ['pk',]
    list_display_links = ['pk',]

admin.site.register(BbCodeModel, BbCodeModelAdmin)
>>>>>>> b755f87e829ee1b394a3d1c7a5ae764b906e867e
