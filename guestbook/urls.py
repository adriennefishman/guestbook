from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guestbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #hello
    #hi

    url(r'^admin/', include(admin.site.urls)),
)
