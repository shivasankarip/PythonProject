from django.conf.urls import patterns, include, url


from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^home/$', 'visitorinfos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
    url(r'^visitor-list/$', 'visitorinfos.views.visitorlist', name='visitorlist'),
    url(r'^employee-list/$', 'visitorinfos.views.employeelist', name='employeelist'),
    url(r'^employee-form/$', 'visitorinfos.views.employeeform', name='employeeform'),
    url(r'^export-excel/$', 'visitorinfos.views.export', name='export'),
    url(r'^date-form/$', 'visitorinfos.views.dateform', name='dateform'),
    url(r'^date-list/$', 'visitorinfos.views.datelist', name='datelist'),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    
    urlpatterns +=static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)