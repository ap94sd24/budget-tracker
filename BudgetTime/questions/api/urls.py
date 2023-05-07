from django.urls import include, path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "question/<slug:slug>/answers/",
        qv.AnswerCreateAPIView.as_view(),
        name="answer-list",
    ),
    path(
        "question/<slug:slug>/answer/",
        qv.AnswerCreateAPIView.as_view(),
        name="answer-create",
    ),
    path(
        "answers/<uuid:uuid>/",
        qv.AnswerCreateAPIView.as_view(),
        name="answer-detail",
    ),
]
