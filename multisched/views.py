from django.shortcuts import render
from django.conf import settings

import django_rq
from .tasks import say_hello

def hello_view(request):
    django_rq.enqueue(say_hello, name=settings.NAME)
    template_name = 'multisched/simple_template.html'
    return render(request, template_name)
