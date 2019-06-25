from django.contrib import admin
from .models import *


class CustomTextInline(admin.StackedInline):
    model = CustomText
    extra = 1


class CustomPageAdmin(admin.ModelAdmin):
    fields = ['text', ]
    inlines = [
        CustomTextInline,
    ]


admin.site.register(CustomPage, CustomPageAdmin)
admin.site.register(GalleryImage)
admin.site.register(GalleryVideo)
admin.site.register(HomeBanner)
