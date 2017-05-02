from django.contrib import admin
from app.models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name','description','Due_Date',)
    list_filter = ('Due_Date','task_type',)
	
    fieldsets = (
	    ('General Task Information', {
		    'fields': ('task_name', 'task_type', 'description', 'customer', 'Due_Date', 'to_do',)
        }),
		('Task Completed?', {
        'classes': ('collapse',),
        'fields': ('completed_date', 'notes', 'duration',),
        'description': 'Please add the detailed of the completed task'
        })
        )	

admin.site.register(Task, TaskAdmin)

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('org_name','city',)
    search_fields = ['org_name','city']
    list_filter = ('org_name','city',)
    fieldsets = (
	    ('General Information', {
		    'fields': ('org_name','phone_number','EMail',)
        }),
		('Address', {
        'classes': ('collapse',),
        'fields': ('street1', 'street2', 'city', 'country','postcode',),
        'description': 'please add an address'
        })
        )	


admin.site.register(Organisation, OrganisationAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'organisation',)
    search_fields = ['department_name']
    list_filter = ('organisation',)

admin.site.register(Department, DepartmentAdmin)

class SiteAdmin(admin.ModelAdmin):
    list_display = ('site_name','organisation',)
    #list_filter = ('organisation',)

admin.site.register(Site, SiteAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_organisation',)
    search_fields = ['customer_name']
    list_filter = ('customer_organisation',)
admin.site.register(Customer, CustomerAdmin)

class CustomerContactAdmin(admin.ModelAdmin):
    search_fields = ['first_name','last_name']
    list_filter = ('customer',)
admin.site.register(CustomerContact, CustomerContactAdmin)

class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)

admin.site.register(TaskType, TaskTypeAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)

admin.site.register(Country, CountryAdmin)
