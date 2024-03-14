from django.contrib import admin
from courses.models import Course, Category
from django.utils.html import mark_safe

class CourseSAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'update_date']
    list_filter = ['subject', 'id']
    search_fields = ['subject']
    readonly_fields = ['my_image']
    def my_image(self,course):
        if course.image:
            return mark_safe(f"<img width='300' src='/static/{course.image.name}' />")
# Register your models here.

admin.site.register(Category)
admin.site.register(Course, CourseSAdmin)
