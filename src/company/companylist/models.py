from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify
# Create your models here.

# Create your models here.
def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)

class Company(models.Model):

    parent = models.ForeignKey('self',blank=True,null=True,related_name='children')
    company_name=models.CharField(max_length=120)
    company_estimated_earnings=models.CharField(max_length=1024)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()


    def __unicode__(self):
        return u"%s "%(self.company_name)


    def __str__(self):
        return self.company_name

    def __unicode__(self):
        return u"%s "%(self.content)


    def __str__(self):
        return self.content


    class Meta:
        ordering = ['parent__id'
                    ]
    def get_absolute_url(self):
        return reverse("company:detail", kwargs={"id": self.id})