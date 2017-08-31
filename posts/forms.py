from django import forms
from django.contrib.auth.models import User
from .models import Profile, Answer, Question, Comment
from django.conf import settings
from django.forms.widgets import DateInput, SelectDateWidget


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class ProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female' ),
    )
    dob = forms.DateField(widget=SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ('bio', 'dob', 'image','gender')


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text',)

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('text','details',)
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
