from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json


@login_required
def index(request):
    return render(request, 'index.html', {})

@login_required
def room(request):
    return render(request, 'chat/room.html')