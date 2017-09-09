from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

router= DefaultRouter()
router.register('hello-viewset',views.testViewset,base_name='hello-viewset')


urlpatterns=[
    url(r'^internal-bot/',views.InternalBotView.as_view()),
    url(r'^reboot-bot/',views.refreshBotView.as_view()),
    url(r'',include(router.urls))
]
