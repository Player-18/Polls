from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from rest_framework.views import APIView


from .models import Question, Choice
from django.urls import reverse

class IndexView(APIView):
    def get(self, request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'app/index.html', context)


class DetailView(View):
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'app/detail.html', {'question': question})


class ResultsView(View):
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'app/results.html', {'question': question})


class EndView(View):
    def get(self, request):
        return render(request, 'app/end.html')


class VoteView(View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        count_question = Question.objects.all().count()
        try:
            selected_choice = question.choices.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'app/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            if question_id < count_question:
                return HttpResponseRedirect(reverse('app:detail', args=(question.id + 1,)))
            else:
                return HttpResponseRedirect(reverse("app:end"))



