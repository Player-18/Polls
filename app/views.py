from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app/results.html', {'question': question})

def end(request):
    return render(request, 'app/end.html')

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    count_question = Question.objects.all().count()
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        if question_id < count_question:
            return HttpResponseRedirect(reverse('app:detail', args=(question.id+1,)))
        else:
            return HttpResponseRedirect(reverse("app:end"))


