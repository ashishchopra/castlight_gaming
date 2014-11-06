from django.conf.urls import include, url
from django.contrib import admin
from gaming import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'castlight_gaming.views.home', name='home'),
    url(r'^index/$', views.index, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
]
