from django.db import models

DIFF_CHOICES=(
	('5','Very Hard'),
	('4','Hard'),
    ('3','Average'),
    ('2','Easy'),
    ('1','Very Easy')
)

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    c1 = models.CharField(max_length=200, default='')
    c2 = models.CharField(max_length=200, default='')
    c3 = models.CharField(max_length=200, default='')
    c4 = models.CharField(max_length=200, default='')
    diff_level=models.CharField(default='5', max_length=1,choices=DIFF_CHOICES)
    answer = models.CharField(max_length=200, default='c1')
    marks = models.IntegerField(default=0)
    
    @classmethod
    def get_answer(qid):
        obj= Question.objects.get(question_id=qid)
        return obj.answer

    def __str__(self):
        return (str(self.question_id) + ".> "  + self.question_text +  "-------------------(problem difficulty is " + self.diff_level+")")
        
    
