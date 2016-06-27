from django.conf.urls import url

from . import views

app_name ='MW'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^summary/$', views.summary, name='summary'),
    url(r'^summary-average/$', views.summary_average, name='summary-average'),
    url(r'^(?P<site_id>[0-9]+)/site_details/$', views.site_details, name='site_details'),
]