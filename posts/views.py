from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Profile, Question, Answer, Comment
from .forms import UserForm, ProfileForm, AnswerForm, QuestionForm
# Create your views here.
#user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
#LockFeature.objects.create(user=request.user ,has_lock=False)
#lockfeature = get_object_or_404(LockFeature,user=request.user)
def myprofile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))
    else:
        user = request.user

        return render(request, 'posts/profile.html',{'user':user})

def user_profile(request,username):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))
    else:
        users = get_object_or_404(User,username=username)
        return render(request, 'posts/userprofile.html',{'users':users})



def update_profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))
    else:
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                profilesave = profile_form.save(commit=False)
                if 'image' in request.FILES:
                    profilesave.image = request.FILES['image']

                user_form.save()
                profile_form.save()
                #messages.success(request, _('Your profile was successfully updated!'))
                return redirect('posts:profile')
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'posts/update_profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })
def add_question(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))
    else:
        if request.method == "POST":
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.user = request.user
                question.created_date = timezone.now()
                question.published_date = timezone.now()
                question.save()
                return redirect('posts:question_list')
        else:
            form = QuestionForm()
        return render(request, 'posts/add_question.html', {'form': form})


def question_list(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))
    else:
        questions = Question.objects.order_by('published_date')
        #answers = Answer.objects.order_by('date')

        return render(request, 'posts/homenew.html', {'questions': questions})

def delete_question(request,pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('posts:question_list')

def delete_answer(request,pk):
    answer = get_object_or_404(Answer,pk=pk)
    value = answer.question.pk
    answer.delete()
    return redirect('posts:question_detail',pk=value)

def update_question(request,pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))
    else:
        print(pk)
        question = get_object_or_404(Question, pk=pk)
        print(question.pk)
        if request.method == 'POST':
            form = QuestionForm(request.POST, instance=question)

            if form.is_valid():
                #que = form.save(commit=False)
                #que.created_date = timezone.now()
                #que.published_date = timezone.now()

                form.save()

                return redirect('posts:question_detail', pk=pk)
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            form = QuestionForm(instance=question)

        return render(request, 'posts/add_question.html', {
            'form': form,

        })

def update_answer(request,pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))
    else:
        print(pk)
        answer = get_object_or_404(Answer, pk=pk)
        print(answer.pk)
        if request.method == 'POST':
            form = AnswerForm(request.POST, instance=answer)

            if form.is_valid():
                #que = form.save(commit=False)
                #que.created_date = timezone.now()
                #que.published_date = timezone.now()

                form.save()

                return redirect('posts:question_detail', pk=answer.question.pk)
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            form = AnswerForm(instance=answer)

        return render(request, 'posts/add_question.html', {
            'form': form,

        })

def question_detail(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))
    else:
        question = get_object_or_404(Question, pk=pk)
        answers = Answer.objects.filter(question = question).order_by('date')
        return render(request, 'posts/post_detailnew.html', {'question': question, 'answers':answers})

def add_answer(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))
    else:
        question = get_object_or_404(Question, pk=pk)
        if request.method == "POST":
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.question = question
                answer.user = request.user
                answer.date = timezone.now()
                answer.save()
                return redirect('posts:question_detail', pk=pk)
        else:
            form = AnswerForm()
        return render(request, 'posts/add_answernew.html', {'form': form, 'question': question})
