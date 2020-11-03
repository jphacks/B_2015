
        

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone

from django.shortcuts import render
from janome.tokenizer import Tokenizer


# def calc(request):
#     val1 = int(request.POST.get('val1'))
#     val2 = int(request.POST.get('val2'))
#     answer = val1 + val2
#     answer = request.POST.get('val1')
#     context = {
#         'answer': answer,
#     }
#     return render(request, 'inquiry.html', context)

def calc(request):
    
    answer = request.POST.get('val1')
    context = {
        'answer': answer,
    }
    return render(request, 'inquiry.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def new(request):
    params = {'word': '', 'name': '', 'form': None}
    if request.method == 'POST':
        form = UserForm(request.POST)
        params['word'] = request.POST['word']
        params['name'] = request.POST['name']
        params['form'] = form
    else:
        params['form'] = UserForm()
    return render(request, 'user/new.html', params)