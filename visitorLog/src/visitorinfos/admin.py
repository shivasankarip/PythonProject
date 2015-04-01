from django.contrib import admin

# Register your models here.
from .models import VisitorInfo

#Admin for the VisitorInfo model.
class VisitorInfoAdmin(admin.ModelAdmin):
    class Meta:
        model=VisitorInfo
    list_display=('first_name','last_name','email','phone','employee_name','purpose_of_visit','timestamp')
        
admin.site.register(VisitorInfo,VisitorInfoAdmin)




