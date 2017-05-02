from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=4)
    
    def __str__(self):
        return self.country_name



class Organisation(models.Model):
    org_name = models.CharField(max_length=300)
    street1 = models.CharField(max_length=100, blank=True)
    street2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.ForeignKey(Country)
    postcode = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    EMail = models.EmailField(max_length=254, blank=True)
    #Status =

    def __str__(self):
        return self.org_name



class Department(models.Model):
    department_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=50,  blank=True)
    EMail = models.EmailField(max_length=254,  blank=True)
    organisation = models.ForeignKey(Organisation)

    def __str__(self):
            return self.department_name

class Site(models.Model):
    site_name = models.CharField(max_length=50)
    street1 = models.CharField(max_length=100, blank=True)
    street2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100,  blank=True)
    country = models.ForeignKey(Country)
    postcode = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    organisation = models.ForeignKey(Organisation)

    
    def __str__(self):
            return self.site_name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_organisation = models.ForeignKey(Organisation)
    customer_department = models.ForeignKey(Department)
    customer_site = models.ForeignKey(Site)
    
    def __str__(self):
            return self.customer_name

class CustomerContact(models.Model):
    customer = models.ForeignKey(Customer)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    EMail = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
            return self.first_name

class TaskType(models.Model):
    type_name = models.CharField(max_length=100)
    #default_interval = models.

    def __str__(self):
            return self.type_name

#class Communication(models.Model):
 #   communication_type = models.ForeignKey(CommType)
  #  date_time = models.DateTimeField(default=datetime.now)
   # subject = models.CharField(max_length=100)
    #summary = models.TextField(max_length=2000)
    #Duration = models.DurationField()
    #followup = models.
    #followup_date
    #followup_done
    #followup_note
    #status =
#class CommsContact (models.Model):

TASK_STATUSES = (
	('n', 'New'),
	('a', 'Completed'),
	('c', 'Cancelled'),
)

class Task(models.Model):
    
    task_name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    Due_Date = models.DateField(("Due Date"), blank=True, null=True)
    to_do = models.TextField(max_length=2000,  blank=True)
    customer = models.ForeignKey(Customer)
    duration = models.DurationField()
    #completed_by = 
    completed_date = models.DateField()
    notes = models.TextField(max_length=2000,  blank=True)
    task_type = models.ForeignKey(TaskType)
    status = models.CharField(max_length=1, choices = TASK_STATUSES, default='n')
    #cancelled_by =
    cancellation_reason = models.TextField(max_length=200, blank=True)
    #cancelled_datetime =
    created_datetime = models.DateTimeField(auto_now_add=True)
    #auto_create_run_id

    #task_owner = 
    #Equipment =
    #
    
    def __str__(self):
        return self.task_name