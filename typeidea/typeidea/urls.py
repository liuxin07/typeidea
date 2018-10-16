
from django.conf.urls import url
from django.contrib import admin

from blog.views import post_list, post_detail
#from config.views import links



from .custom_site import custom_site

urlpatterns = [
    url(r'^$', post_list, name='index'),
    url(r'^category/(?P<category_id>\d+)/$', post_list, name='category'),
    url(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='detail'),
    #url(r'^links/$', links),
    url(r'^admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
]
