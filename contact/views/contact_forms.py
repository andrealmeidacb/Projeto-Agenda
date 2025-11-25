from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator


def create(request):
    if request.method == 'POST':
        print()
        print(request.method)
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))
        print()
    context = {

    }

    return render(
        request,
        'contact/create.html',
        context,
    )