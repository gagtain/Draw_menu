from django.contrib import admin
from .models import *
# Register your models here.


class PostCodesAdmin(admin.ModelAdmin):
    exclude = ('scr',)


admin.site.register(MenuItem, PostCodesAdmin)
admin.site.register(Menu, PostCodesAdmin)