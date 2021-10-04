from django.shortcuts import render, redirect
from .forms import add_question_form
from .models import Question
import random
# Create your views here.


def add_question_view(request):    
    if request.user.is_staff:
        form=add_question_form()
        if request.method=='POST':
            form=add_question_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'questions/add_question.html',context)
    else: 
        return render(request,'questions/add_no.html') 


def home(request):
    if request.method == 'POST':

        score = 0 
        for elt in request.POST:
            #we looking for the answer of a given question
            get_answer = Question.objects.filter(question=elt).values('answer')
            #We extract the answer as keys of a dictionary 
            for DICT in list(get_answer):
                get_answer = DICT['answer']

            if request.POST.get(elt) == get_answer:
                score +=1
            if score > 3:
                mention = 'Feliciations!'    
            else:
                mention ='Vous devez reussir à au moins 4 questions sur 5!'    
        context= {
            'test' : score,
            'mention':mention,
            'echec': 5 - score
        }
        return render(request,'questions/result.html',context)
    else:
        questions=Question.objects.all().order_by('?')[:5] #randomnly getting 5 questions
        context = {
            'questions':questions
        }
        return render(request,'home.html',context)