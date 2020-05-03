from django.db import models
from QuestionSetter.models import *

class Test(models.Model):
    test_id = models.CharField(max_length = 20,primary_key=True)
    name = models.CharField(max_length=200)
    test_time = models.IntegerField(default = 60)
    test_url = models.CharField(max_length = 20, default = '')


    def __str__(self):
        return str(self.test_id + " " + self.name)

class Association(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    @classmethod
    def get_test_question_id(cls, test_id):
        association_obj = cls.objects.filter(test_id=test_id)
        question_id_list = [
            obj.question.question_id for obj in association_obj]
        return question_id_list

    def __str__(self):
        return str(self.test) + " contains " + str(self.question)
