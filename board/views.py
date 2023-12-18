from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Board
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return afterlogin(request)
        else:
            return render(request, 'board/board_login.html', {'error_message': '아이디 혹은 비밀번호가 잘못되었습니다.'})
    return render(request, 'board/board_login.html')

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board' : board}
    return render(request, 'board/board_detail.html', context)

def afterlogin(request):
   board_list = Board.objects.order_by('create_date')
   context = {'board_list': board_list}
   return render(request, 'board/board_list.html',context)

class create(generic.CreateView):
    model = Board
    fields = ['subject', 'content', 'create_date']
    success_url = reverse_lazy(afterlogin)
    template_name_suffix = '_create'

    