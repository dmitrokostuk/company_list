from django.conf.urls import url
from django.contrib import admin

from .views import (
    company_create,
    company_edit,
    company_list,
    company_delete,
    company_detail,

	)

urlpatterns = [
	url(r'^$', company_list ,name='company'),
    url(r'^create/$', company_create),
    url(r'^(?P<slug>[\w-]+)/$',company_detail , name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', company_edit, name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', company_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]