from django.db import models


class Question (models.Model):
    course_id =  models.IntegerField(default=0)
    question = models.CharField(max_length=255, default='notDefined')
    answer = models.TextField(blank=True)
    class Meta:
        db_table = 'questions'
    def __str__(self):
        return self.question    
 
class Course (models.Model):
    name = models.CharField(max_length=255, default='unknownCourse')
    portal = models.CharField(max_length=255, default='notKnown')
    class Meta:
        db_table = 'courses'
    def __str__(self):
        return self.name

class Portal (models.Model):
    name = models.CharField(max_length=255, default='unknownPortal')
    url = models.TextField(blank=True)
    token = models.TextField(blank=True)
    class Meta:
        db_table = 'portals'
    def __str__(self):
        return self.name
    
class Settings (models.Model):
    botToken = models.TextField(blank=True)
    class Meta:
        db_table = 'settings'
