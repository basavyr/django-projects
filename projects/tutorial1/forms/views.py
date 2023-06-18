from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "list": [1, 2, 3]
    }

    return render(request, 'forms/forms.html', context)
