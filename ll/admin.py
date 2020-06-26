from django.contrib import admin

from .models import Project, Lesson, Projectnumber, Projectname, Client, Projectlocation, Marketsector, Memo

class Project_numberAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Project_nameAdmin(admin.ModelAdmin):
    list_display = ('name', 'projectnumber')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'projectnumber')

class Project_locationAdmin(admin.ModelAdmin):
    list_display = ('name', 'projectnumber')

class Market_sectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'projectnumber')

class MemoAdmin(admin.ModelAdmin):
    list_display = ('name', 'projectnumber')

class ProjectList(admin.ModelAdmin):
    list_display = ( 'project_name', 'project_number' )
    list_filter = ( 'project_name', 'project_number')
    search_fields = ('project_name', )
    ordering = ['project_name']


class LessonList(admin.ModelAdmin):
    list_display = ( 'projectname', 'projectnumber', 'author')
    list_filter = ( 'projectname', 'projectnumber')
    search_fields = ('author', )
    ordering = ['author']

admin.site.register(Project, ProjectList)
admin.site.register(Lesson, LessonList)
admin.site.register(Projectname, Project_nameAdmin)
admin.site.register(Projectnumber, Project_numberAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Projectlocation, Project_locationAdmin)
admin.site.register(Marketsector, Market_sectorAdmin)
admin.site.register(Memo, MemoAdmin)