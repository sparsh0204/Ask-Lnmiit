from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^profile/myprofile$', views.myprofile, name='profile'),
    url(r'^profile/update$', views.update_profile, name='update_profile'),
    url(r'^profile/(?P<username>[-\w]+)/$', views.user_profile, name='user_profile'),
    url(r'^$', views.question_list, name='question_list'),
    url(r'^add_question/$', views.add_question, name='add_question'),
    url(r'^post/(?P<pk>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.delete_question, name='delete_question'),
    url(r'^post/(?P<pk>\d+)/answer/$', views.add_answer, name='add_answer'),
    url(r'^post/(?P<pk>\d+)/answer/edit/$', views.update_answer, name='update_answer'),
    url(r'^post/(?P<pk>\d+)/answer/delete/$', views.delete_answer, name='delete_answer'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.update_question, name='update_question'),

    #url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
