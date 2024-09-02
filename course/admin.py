from django.contrib import admin
from course.models import Season, Session, Course, Category
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

admin.site.register(Category)

class SessionAdmin(NestedStackedInline):
    model = Session
    extra = 0


class SeasonAdmin(NestedStackedInline):
    model = Season
    extra = 0
    inlines = (SessionAdmin,)


@admin.register(Course)
class CoursesAdmin(NestedModelAdmin):
    list_display = ('title', 'teacher', 'time', 'price')
    list_filter = ('created_at',)
    search_fields = ('title',)
    readonly_fields = ('slug',)
    inlines = (SeasonAdmin,)


