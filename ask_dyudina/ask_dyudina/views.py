# -*- coding: utf-8 -*-

from django.shortcuts import render


def index(request):
    greeting = 'Привет, мир!'
    get_params = request.GET.items()
    post_params = request.POST.items()
    return render(request, 'index.html', {'greeting': greeting,
                                          'get_params':get_params,
                                          'post_params':post_params})




