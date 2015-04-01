from django.db import models

from django.utils.encoding import smart_unicode
# Create your models here.
# VisitorInfo model which stores the data in the db.
class VisitorInfo(models.Model):
    first_name=models.CharField(max_length=120, null=True, blank=True)
    last_name=models.CharField(max_length=120, null=True, blank=True)
    email=models.EmailField()
    phone=models.BigIntegerField(max_length=10, null=True, blank=True)
    employee_name=models.CharField(max_length=120, null=True, blank=True)
    purpose_of_visit=models.CharField(max_length=200, null=True, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    
    
    def __unicode__(self):
        return smart_unicode(self.email)
    
    
    


    
