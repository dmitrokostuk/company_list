from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify
# Create your models here.

# Create your models here.
class Company(models.Model):

    parent = models.ForeignKey('self',blank=True,null=True)
    company_name=models.CharField(max_length=120)
    company_estimated_earnings=models.CharField(max_length=1024)


    def __unicode__(self):
        return u"%s "%(self.company_name)

