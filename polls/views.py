from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question


def index(request):
    last_questions_list = Question.objects.order_by("-pub_date").all()[:5]
    # print(last_questions_list.query)
    context = {
        "latest_question_list": last_questions_list
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # we can also use get_object_or_404 to do the same functionality given below
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
