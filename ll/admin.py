from django.contrib import admin

from .models import Project, Lesson


class ProjectList(admin.ModelAdmin):
    list_display = ( 'project_name', 'project_number' )
    list_filter = ( 'project_name', 'project_number')
    search_fields = ('project_name', )
    ordering = ['project_name']


class LessonList(admin.ModelAdmin):
    list_display = ( 'project_name', 'project_number', 'author')
    list_filter = ( 'project_name', 'project_number')
    search_fields = ('author', )
    ordering = ['author']

admin.site.register(Project, ProjectList)
admin.site.register(Lesson, LessonList)
