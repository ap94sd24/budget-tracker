from rest_framework import viewsets 

from questions.api.serializers import QuestionSerializer
from questions.models import Question

class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all().order_by("-created_at")
  serializer_class = QuestionSerializer