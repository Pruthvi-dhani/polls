from django.http import HttpResponse
from .models import Question


def index(request):
    last_questions_list = Question.objects.order_by('-pub_date').all()[:5]
    # print(last_questions_list.query)
    output = ', '.join([q.question_text for q in last_questions_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
