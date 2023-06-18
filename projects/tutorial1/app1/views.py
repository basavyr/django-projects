from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def hello(request):
    client_ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')

    context = {
        'client_ip': client_ip,
        'user_agent': user_agent
    }

    return render(request, 'hello.html', context)
