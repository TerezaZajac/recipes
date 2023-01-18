from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Tag)
admin.site.register(Unit)
admin.site.register(Ingredience)
admin.site.register(Recipe)
admin.site.register(Course)
