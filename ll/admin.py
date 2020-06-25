from django.contrib import admin

from .models import Project, Lesson, Project_number, Project_name, Client, Project_location, Market_sector

class Project_numberAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Project_nameAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_number')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_name')

class Project_locationAdmin(admin.ModelAdmin):
    list_display = ('name', 'client')

class Market_sectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_location')

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
admin.site.register(Project_name, Project_nameAdmin)
admin.site.register(Project_number, Project_numberAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Project_location, Project_locationAdmin)
admin.site.register(Market_sector, Market_sectorAdmin)