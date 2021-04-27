from collections import defaultdict

from django.shortcuts import render

# Create your views here.

from polls.models import Question, Choice


def index(request):
    questions = Question.objects.all()

    context = {
        "questions": questions,

    }
    # print(questions[0].choice_set.all())
    return render(request, "polls/index.html", context)


