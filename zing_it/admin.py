from django.contrib import admin

from zing_it.models import AccessRecord, Company, Employee, Project, Topic, Webpage

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Company)  # Register the Company model with the admin site
admin.site.register(Employee)  # Register the Employee model with the admin site
admin.site.register(Project)  # Register the Project model with the admin site
admin.site.site_header = "Zing It Admin"
