from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^internal-bot/',views.InternalBotView.as_view()),
]
