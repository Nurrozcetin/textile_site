from django.contrib import admin
from .models import Category, Item

@admin.register(Item)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "fabric", "category")
    readonly_fields = ("fabric",)
    search_fields = ("title", "fabric",)

    def category(self, obj):
        html = ""
        for category in obj.categories.all():
            html += category.name + " "
        return html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
