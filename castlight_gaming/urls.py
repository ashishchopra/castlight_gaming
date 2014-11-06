from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from gaming import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'castlight_gaming.views.home', name='home'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='login'),
    url(r'^index/$', views.index, name='detail'),
    url(r'^first_page/$', views.show_random_user_profile, name='detail'),
    url(r'^gaming/level/$', views.index, name='level'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.user_login, name='login'),
]


