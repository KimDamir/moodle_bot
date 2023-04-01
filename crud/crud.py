from crud.models import Question

def create(course_id=int, question_text=str, answer=str):
    q=Question()
    q.course_id=course_id 
    q.question=question_text 
    q.answer=answer
    q.save()
   
def read(question_id=int):
    return Question.objects.get(id=question_id)
    
      
def update(question_id=int,course_id=0, question_text="", answer=""):
    q=Question.objects.get(id=question_id)
    if(course_id != 0):
        q.course_id=course_id
    if(question_text != ""):
        q.question=question_text
    if(answer != 0):
        q.answer=answer
    q.save()           
    
    
def delete(question_id):
    q=Question.objects.get(id=question_id)
    q.delete()