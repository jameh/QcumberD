from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    

    # Uncomment the next line to enable the SOLUS screen scraper
    url(r'^solus_scraper/', include('solus_scraper.urls')),

    # Uncomment the next line to enable checking of enrollment
    url(r'^enrollment/', include('enrollment.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('course_catalog.urls')),
)
