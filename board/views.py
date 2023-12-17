from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Board
from django.views import generic
from django.urls import reverse_lazy

# def index(request):
    # return HttpResponse("Hello")

def index(request):
   board_list = Board.objects.order_by('create_date')
   context = {'board_list': board_list}
   return render(request, 'board/board_list.html',context)

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board' : board}
    return render(request, 'board/board_detail.html', context)

class create(generic.CreateView):
    model = Board
    fields = ['subject', 'content', 'create_date']
    success_url = reverse_lazy('board_list')
    template_name_suffix = '_create'

    