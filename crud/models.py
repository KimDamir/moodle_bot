from django.db import models


class Question (models.Model):
    id = models.IntegerField(blank=True)
    course_id =  models.IntegerField()
    question = models.CharField(max_length=255)
    answer = models.TextField()
    class Meta:
        db_table = 'questions'
    def __str__(self):
        return self.question    
 
class Course (models.Model):
    id = models.IntegerField
    name = models.TextField
    class Meta:
        db_table = 'courses'
    def __str__(self):
        return self.name          