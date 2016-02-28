from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

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
    return render(request, "company_form.html", context )

def company_edit(request,id=None):
    instance  = get_object_or_404(Company,id=id)
    form = Company_Add_Form(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "company.name": instance.company_name,
        "instance":instance,
        "form":form
    }
    return render(request, "company_form.html",context )


def company_detail(request, id = None):
    instance  = get_object_or_404(Company,id=id)
    context = {
        "company_name":instance.company_name,
        "instance": instance
    }
    return render(request, "company_detail.html",context )

def company_list(request):
    queryset = Company.objects.all()
    context = {
                "company_list": queryset,
                "company_name":"List"

               }
    return render(request, "company_list.html",context )


def company_delete(request):
    return render(request, "post_form.html" )