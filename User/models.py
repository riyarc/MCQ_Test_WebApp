from django.db import models
from django.contrib.auth.models import User
from TestSetter.models import *
from random import shuffle
from datetime import datetime, timedelta, timezone

class Contestant(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ongoing_test = models.IntegerField(default=0)

    def set_ongoing_test(self, test_id):
        self.ongoing_test = test_id
        self.save()

    def get_ongoing_test(self):
        return self.ongoing_test

    def __str__(self):
        return str(self.user)


class UsersTest(models.Model):

    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    contestant = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    current_que_id = models.IntegerField(default=1)
    first_login = models.BooleanField(default=False)
    que_array = models.TextField(default="", null=True, blank=True)
    ans_array = models.TextField(default="", null=True, blank=True)
    test_progress = models.TextField(default="", null=True, blank=True)
    test_submitted = models.IntegerField(default=0)
    test_started = models.BooleanField(default = False)
    completion_time = models.DateTimeField(default = datetime.now() + timedelta(hours = 3))

    @classmethod
    def get_user_tests(cls, contestant_id):
        user_test_objs = UsersTest.objects.filter(contestant_id=contestant_id)
        return [objs.test for objs in user_test_objs]

    def get_answer(self, index):
        answers = []
        if(len(self.ans_array)==0):
            for id in [int(index) for index in self.que_array.split(" ")]:
                answers.append('c0')
            self.ans_array = ' '.join(answers)
            self.save()
        value = self.ans_array.split(" ")[index]
        return value

    def get_answer_list(self):
        return self.ans_array.split(" ")

    def set_answer(self, answers):
        self.ans_array = answers
        self.save()

    def get_questions(self):
        question_list = []
        for id in [int(index) for index in self.que_array.split(" ")]:
            question_list.append(Question.objects.get(pk=id))
        return question_list

    def set_questions(self, question_list):
        shuffle(question_list)
        question_indexes_s = [str(element) for element in question_list]
        self.que_array = ' '.join(question_indexes_s)
        self.save()

    def get_question_indices(self):
        return [int(index) for index in self.que_array.split(" ")]

    def get_curr_qid(self):
        return self.current_que_id

    def get_test_submitted(self):
        return self.test_submitted

    def set_login(self, value):
        self.first_login = value
        self.save()

    def set_curr_qid(self, value):
        self.current_que_id = value
        self.save()

    def set_score(self, value):
        self.score = value
        self.save()

    def set_test_submitted(self):
        self.test_submitted = 1
        self.save

    def update_answer(self, index, value):
        self.ans_array = self.ans_array.split(" ")
        self.ans_array[index] = value
        self.ans_array = ' '.join(self.ans_array)
        self.save()

    def set_visited(self, index):
        self.ans_array = self.ans_array.split(" ")
        if self.ans_array[index] == 'c0':
            self.ans_array[index] = 'c'
        self.ans_array = ' '.join(self.ans_array)
        self.save()

    def __str__(self):
        return str(self.test) + " <===> " + str(self.contestant)
