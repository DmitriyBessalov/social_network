from django.shortcuts import render
from django.http import HttpResponse
import os


def index(request):
    return render(request, 'index.html', {})


def git_pull(request):
    shell = os.system(
        'git reset --hard origin/master && git pull https://github.com/DmitriyBessalov/social_network.git')
    return HttpResponse(shell)
