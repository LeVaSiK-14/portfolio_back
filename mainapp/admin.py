from django.contrib import admin
from mainapp.models import(
    AboutMe, ProjectsCategory, Project,
    ProjectsImage, Contact
)


class ProjectImageAdmin(admin.TabularInline):
    model = ProjectsImage
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin, ]


admin.site.register(AboutMe)
admin.site.register(ProjectsCategory)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact)