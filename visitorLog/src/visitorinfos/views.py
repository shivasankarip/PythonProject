
# import django important modules ro render response and receive request
#import xlwt to write to excel sheet
#import datetime to use the datetime module for comparing dates
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
import xlwt
from datetime import datetime 

# Create your views here.
#import the forms and models 
from .forms import VisitorInfoForm
from .models import VisitorInfo

#function def for home which will have a registeration form and save the details to db
def home(request):
#get the form request   
    form=VisitorInfoForm(request.POST or None)
    
#check for the form validity. if valid save it in the db and send a success message back to the browser    
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        messages.success(request,' Welcome to UCSC !! Thank you for registering the visitor info')
        #this sends a success message to the browser
       
    
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))

# to get all the visitor list from the db
def visitorlist(request):
    context = RequestContext(request)
    visitor_list= VisitorInfo.objects.all()
    context_dict={'visitorinfos':visitor_list}
    
    return render_to_response('visitorlist.html',context_dict,context)

# to open the employye form 
def employeeform(request):
    return render(request, 'employeelist.html')

# to get the employee list from the db for the employee name from the post request    
def employeelist(request):
    context=RequestContext(request)
    context_dict={}
    try:
        name=request.GET['employee']
        visitors=VisitorInfo.objects.all()
        value=[x for x in visitors if (x.employee_name==name)]
        context_dict={'emplist':value}
        if not value:
            raise KeyError
    except KeyError:
        messages.error(request,"No results found.Try again with a valid value !!")    
    return render_to_response('employeelist.html',context_dict,context)

# to get the date form page    
def dateform(request):
    return render(request, 'datelist.html')

# to get the list of visitors from db for the particular date interval
def datelist(request):
    context=RequestContext(request)
    context_dict={}
    try:
        t1=datetime.strptime(request.GET['datefrom'] , '%Y-%m-%d')
        t2=datetime.strptime(request.GET['dateto'], '%Y-%m-%d')
        visitors=VisitorInfo.objects.all()
        value=[x for x in visitors
               if checkdate(x,t1,t2)]
        context_dict={'datelist':value}
        if not value:
            raise TypeError
    except ValueError:
        messages.error(request,"please provide a valid date!!")
    except TypeError:
        messages.error(request,"No results matching these dates. Try again with different dates !!")
    return render_to_response('datelist.html',context_dict,context)


# a function to check the date from the db with the provided date from the form.
def checkdate(x,t1,t2):
    dbdate=x.timestamp
    if(dbdate.date() >t1.date() and dbdate.date() < t2.date()) or (dbdate.date() == t1.date() or dbdate.date() == t2.date()):
        return True    
    else:
        return False
    
# function to export the data from the db and store it in as a Excel sheet    
def export(request):
    context=RequestContext(request)
    visitorlist= VisitorInfo.objects.all()
    fo=open('file.txt','w+')
    data=[]
    value={}
    for visitor in visitorlist:
        value={'visitor first name':visitor.first_name,
               'visitor last name':visitor.last_name,
               'Email id':visitor.email,
               'phone number':visitor.phone,
               'Employee name':visitor.employee_name,
               'Purpose of visit':visitor.purpose_of_visit}
        data.append(value)

    
    w = xlwt.Workbook()
    ws = w.add_sheet('sheet1')
    columns = list(data[0].keys()) 
    for i,row in enumerate(data):
        for j, col in enumerate(columns):
            ws.write(i, j, row[col])
    
    w.save('data.xls')
    
    messages.success(request,'Tha data have been successfully stored to data.xls file')
    
    return render_to_response('export-excel.html',locals(),context)