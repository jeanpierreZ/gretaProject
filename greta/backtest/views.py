from django.shortcuts import render


def index(request):
    context = {'content': 'Bonjour !'}
    return render(request, 'backtest/index.html', context)
