from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('TenderITApp.urls')),
    url(r'^inplaceeditform/', include('inplaceeditform.urls'))
 ]
