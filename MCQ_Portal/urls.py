from django.conf.urls import url, include
from django.contrib import admin
from QuestionSetter.views import *
from TestSetter.views import *
from User.views import *
# from registration.backends.default import urls

admin.site.site_header = 'MCQ Portal'
urlpatterns = [
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^tests/(?P<test_id>\d+)/score/$', show_marks, name='score'),
    url(r'^ans_submit/', ans_submit, name='ans_submit'),
    url(r'^q_submit/', navigate_question, name='q_submit'),
    url(r'^tests/(?P<test_id>\d+)/(?P<id>\d+)/$', question, name='contest_que'),
    url(r'^tests/$', show_test_list, name='tests'),
    url(r'^tests/(?P<test_id>\d+)/$', show_test_details, name='test_details'),
    url(r'^tests/(?P<test_id>\d+)/testcompleted/$', test_completed, name='test_completed'),
]
