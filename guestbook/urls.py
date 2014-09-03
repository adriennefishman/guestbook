from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from guestbook import views

from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^update/$', views.update),
)

# urlpatterns = patterns('',
#     # Examples:
#     url(r'^$', 'guestbook.views.index', name='index'),
# #     # url(r'^blog/', include('blog.urls')),

# #     url(r'^admin/', include(admin.site.urls)),
# )

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]
