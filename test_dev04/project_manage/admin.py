from django.contrib import admin

from project_manage.models import Project, Module


# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "status", "update_time", "create_time"]


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["project", "name", "describe", "update_time", "create_time"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)

