from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from questionbox.models import Question
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
# index.html currently displays latest_question_list   
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'questionbox/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at detail for %s" % question_id)





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
    
