from QuestionSetter.models import *
from TestSetter.models import *
from User.models import *
from django.contrib.auth.models import User

# UTILITY PACKAGES
# =======================================================
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def HttpError(**args):
    error = args['error']
    try:
        title = args['title']
    except KeyError:
        title = "Error"
    context = {
        "error": error,
        "title": title
    }
    return render(args['request'], 'questions/error.html', context)


def question_pk_list(request):
    # Returns the list of questions
    try:
        list_key = list(Question.objects.values_list("pk", flat=True))
    except ObjectDoesNotExist as err:
        return HttpError(request=request,
                         error="Database Error: ObjectDoesNotExist",
                         details=err)
    return list_key


def total_questions(request):
    # Return number of questions
    try:
        total = int(Question.objects.all().count())
    except ObjectDoesNotExist as err:
        return HttpError(request=request,
                         error="Database Error: ObjectDoesNotExist",
                         details=err)
    return total