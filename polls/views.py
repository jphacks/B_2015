
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone

from django.shortcuts import render
from django.http import HttpResponse

# application/bungou.pyをインポートする
from .application import bungou

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries


# ajaxでurl指定したメソッド
def call_bungou(req):
    if req.method == 'GET':
        # bungo.pyのsearch()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        bungou.search(req.GET.get("input_data"))

        # bungo.pyの中に新たに記述したメソッド(return_text())を呼び出す。
        data = bungou.return_text()
        # 受け取ったデータをhtmlに渡す。
        return HttpResponse(data)


# 使ってないけどurls修正だるいのでとりあえず放置
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

def login(req):
    return render(req, 'login.html')

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
