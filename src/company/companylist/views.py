from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.


def company_create(request):
    return render(request, "post_form.html" )

def company_edit(request):
    return render(request, "post_form.html" )


def company_detail(request):
    return render(request, "post_form.html" )

def company_list(request):
    return render(request, "company_list.html" )


def company_delete(request):
    return render(request, "post_form.html" )