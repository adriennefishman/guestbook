from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from guestbook import views

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'guestbook.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
