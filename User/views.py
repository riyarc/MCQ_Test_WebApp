from QuestionSetter.models import *
from TestSetter.models import *
from User.models import *
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone

# UTILITY PACKAGES
# =======================================================
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from QuestionSetter.views import *
from TestSetter.views import *


def get_contestant(request):
    # Returns contestant for given user
    try:
        current_user = User.objects.get(username=request.user)
    except ObjectDoesNotExist as err:
        return HttpError(request=request,
                         error="Not logged in the system, Please go back and log in!",
                         details=err)
    try:
        # Get contestant corresponding to user
        contestant = Contestant.objects.get(user=current_user)
    except ObjectDoesNotExist:
        # Make a new contestant
        contestant = Contestant(user=current_user)
        contestant.save()
    return contestant


def index(request):
    # Main User page
    app_name = getattr(settings, "APP_NAME", None)
    context = {
        "title": "Welcome to MCQ Portal",
        "app_name": app_name
    }
    return render(request, 'questions/index.html', context)


@login_required
def show_marks(request, test_id):
    user_test = get_user_tests(request, test_id)
    question_indexes = user_test.get_question_indices()
    answer_array = user_test.get_answer_list()
    total_marks = 0
    total_ques = len(question_indexes)
    solutions = list()
    correct_ans = 0
    for i in range(total_ques):
        cur_que_index = i
        cur_que = question_indexes[cur_que_index]
        question = Question.objects.get(pk=cur_que)
        print(question)
        question_score = question.marks
        answer = answer_array[i]
        if answer != 'c0':
            solutions.append((i + 1, question, answer, eval(f'question.{answer}'), eval(f'question.{question.answer}')))
           
        if answer == 'c0':
            solutions.append((i + 1, question, answer, "No Selection Made" , eval(f'question.{question.answer}')))
        
        if answer == question.answer:
            total_marks = total_marks + question_score
            correct_ans += 1
    user_test.set_score(total_marks)
    context = {
        'score': user_test.score,
        'title': "View Marks",
        'solutions' : solutions,
        'correct_ans' : correct_ans,
        'wrong_ans' : total_ques - correct_ans,
        'total_ques' : total_ques, 
    }
    return render(request, 'questions/score.html', context)


@login_required
def question(request, id, test_id):
    # view question with id
    user_test = get_user_tests(request, test_id)
    if not user_test.test_submitted and not user_test.test_started:
        user_test.completion_time = datetime.now() + timedelta(hours = 3)
        user_test.test_started = True
        user_test.save()
    print(str(user_test.completion_time)[:19])
    cleaned_date = str(user_test.completion_time)[:19].split()
    java_script_date_time = cleaned_date[0] + 'T' + cleaned_date[1] + 'Z'
    print(java_script_date_time)
    question_indexes = user_test.get_question_indices()
    question_id = int(id)
    question_count = len(user_test.get_question_indices()) + 1
    if question_id <= question_count :
        try:
            question_num = question_id - 1
            question_pk = question_indexes[question_num]
        except IndexError as err:
            return HttpError(request=request,
                             error="Question index out of range!",
                             details=err)
        try:
            question = Question.objects.get(pk=question_pk)
        except ObjectDoesNotExist as err:
            return HttpError(request=request,
                             error="Database Error: ObjectDoesNotExist",
                             details=err)
        answer = user_test.get_answer(question_num)
        user_test.set_curr_qid(id)
        questions = user_test.get_questions()
        answers = user_test.get_answer_list()
        merged_list = [(1+i, questions[i], answers[i]) for i in range(0, len(answers))]
        context = {
            "answer": answer,
            "question": question,
            "merged_list":merged_list,
            "len":len(questions),
            "id": id,
            "test_id": test_id,
            "total": question_count-1,
            "title": "Question " + id,
            'expiry_age' : java_script_date_time,
        }
        test_submitted = user_test.get_test_submitted()
        if test_submitted:
            return render(request, 'questions/test_submitted.html')
        else:
            return render(request, 'questions/question.html', context)


@login_required
def ans_submit(request):
    contestant = get_contestant(request)
    test_id = contestant.get_ongoing_test()
    userstest = get_user_tests(request, test_id)
    cur_question_num = (userstest.get_curr_qid()) - 1
    answer = request.POST['ans']
    userstest.update_answer(cur_question_num, answer)
    return HttpResponse("OK")


@login_required
def navigate_question(request):
    contestant = get_contestant(request)
    test_id = contestant.get_ongoing_test()
    userstest = get_user_tests(request, test_id)
    question_queue = userstest.get_curr_qid()
    userstest.set_visited(int(question_queue)-1)
    if request.POST['type'] == 'next':
        if int(question_queue) <= userstest.current_que_id:
            userstest.set_curr_qid(int(question_queue) + 1)
    else:
        userstest.set_curr_qid(int(question_queue) - 1)
    return HttpResponse("OK")


def get_tests(request, contestant):
    tests = UsersTest.get_user_tests(contestant.id)
    return tests


def get_user_tests(request, test_id):
    contestant = get_contestant(request)
    userstest = UsersTest.objects.get(contestant=contestant, test_id=test_id)
    return userstest


@login_required
def show_test_list(request):
    contestant = get_contestant(request)
    tests = get_tests(request, contestant)
    return render(request, 'questions/tests.html', {'tests': tests})


@login_required
def show_test_details(request, test_id):
    contestant = get_contestant(request)
    contestant.set_ongoing_test(test_id)
    user_test = get_user_tests(request, test_id)
    test_ques_association = Association.objects.filter(test_id=test_id)
    questions = [objs.question for objs in test_ques_association]
    q_str_list = [str(question.question_id) for question in questions]
    if user_test.first_login is False:
        curr_id = user_test.get_curr_qid()
    else:
        curr_id = 1
    if user_test.first_login is False:

        user_test.set_questions(q_str_list)
        user_test.set_answer(q_str_list)
        questions = user_test.get_questions()
        user_test.set_login(True)
    else:
        questions = user_test.get_questions
    context = {
        'questions': questions,
        'test_id': test_id,
        'curr_id': curr_id
    }
    return render(request, 'questions/test_details.html', context)


@login_required
def test_completed(request, test_id):
    user_test = get_user_tests(request, test_id)
    user_test.set_test_submitted()
    return render(request,
                  'questions/test_completed.html',
                  {'test_id': test_id})
