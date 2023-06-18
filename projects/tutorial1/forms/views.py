from django.shortcuts import render


def index(request):

    return render(request, 'forms/forms.html')


def show_forms(request):
    context = {
        "my_list": [1, 2, 3]
    }

    return render(request, 'forms/show_forms.html', context)
