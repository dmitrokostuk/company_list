from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your views here.
from .forms import Company_Add_Form
from .models import Company



def company_create(request):
    form = Company_Add_Form(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
            "form":form,
        }
    return render(request, "company_form.html", context, )

def company_edit(request,id=None):
    instance  = get_object_or_404(Company,id=id)
    form = Company_Add_Form(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url(),reverse('edit'))

    context = {
        "company.name": instance.company_name,
        "instance":instance,
        "form":form
    }
    return render(request, "company_form.html",context, )


def company_detail(request, id = None):
    instance  = get_object_or_404(Company,id=id)
    context = {
        "company_name":instance.company_name,
        "instance": instance
    }
    return render(request, "company_detail.html",context )

def company_list(request):
    queryset_list = Company.objects.all()
    paginator = Paginator(queryset_list,5)
    page = request.GET.get('page')
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        queryset_list = paginator.page(1)
    except EmptyPage:
        queryset_list = paginator.page(paginator.num_pages)
    context = {
                "company_list": queryset_list,
                "company_name":"List",

               }
    return render(request, "company_list.html",context )








def company_delete(request, id=None):
    instanse = get_object_or_404(Company,id=id)
    instanse.delete()
    messages.success(request,"Company Deleted")
    return redirect("company:company" )