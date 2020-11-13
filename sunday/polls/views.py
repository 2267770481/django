from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# fbv
def index(request):
    latest_question_list = Question.objects.order_by('-date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)  # 这里的pk 就是表里的id(django默认提供)
    return render(request, 'polls/detail.html', {'question': question})


@require_POST
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        choice = Choice.objects.get(pk=request.POST['choice'])
    except:
        return HttpResponse('该问题现在还没有选项')
    else:
        choice.votes += 1
        choice.save()
    return HttpResponseRedirect(reverse('polls:result', args=(pk,)))  # 注意重定向那里是冒号 :


def result(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/result.html', {'question': question})


# cbv
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'
