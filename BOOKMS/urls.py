from django.conf.urls import patterns, include, url
from bookapp.views import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BOOKMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'book/create/$', create_book, name='create_book'),
    url(r'book/list/$', list_book, name='list_book'),
    url(r'book/edit/(?P<id>[^/]+)/$', edit_book, name='edit_book'),
    url(r'book/view/(?P<id>[^/]+)/$', view_book, name='view_book'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()