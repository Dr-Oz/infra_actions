from django.shortcuts import render


def index(request):
    return render(request, 'infra_app/index.html', {'content': 'У меня получилось!'})


def second_page(request):
    return render(request, 'infra_app/second_page.html', {'content': 'А это вторая страница!'})
