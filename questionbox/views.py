from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from .models import Question, Answer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# index.html currently displays latest_question_list   
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'questionbox/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionbox/detail.html',{ 'question':question })

def star(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        starred_answer = question.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'questionbox/detail.html', {
            'question': question,
            'error_message': "If you're not gonna star something why'd you click this?",
        })
    else:
        starred_answer.star += 1
        starred_answer.save()
    return HttpResponseRedirect(reverse('questionbox:star', args=(question_id, )))




# # @login_required
# def profile_detail(request):
#     return render(request, 'questionbox/profile_detail.html', {'questions': request.user.questions})
    
# def question_detail(request, question_id):
#     response = "You're looking at question_detail for question %s."
#     return HttpResponse(response % question_id)


# # def question_list(request):
# #     question_list = Question.objects.all()
# #     return render(request, 'questionbox/question_list.html', {'questions': question_list})
    
# # @login_required    
# def add_answer(request, question_id):
#     return render(request, 'questionbox/add_answer_form.html', {'questions': add_answer})

# # @login_required    
# def add_question(request):
#     return render(request, 'questionbox/add_question_form.html',{'questions': add_question})
    
