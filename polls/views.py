from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question as ModelQuestion, Choice as ModelChoice

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)



# ------------------------------custom or internal views-------------------------

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import Question

from .serializers import GroupSerializer, UserSerializer, Question as QuestionSerilizer, Choise as ChoiceSerializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated] 

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = ModelQuestion.objects.all()
    serializer_class = QuestionSerilizer
    permission_classes = [permissions.IsAuthenticated]

class ChoiseViewSet(viewsets.ModelViewSet):
    queryset = ModelChoice.objects.all()
    serializer_class = ChoiceSerializers
    permission_classes = [permissions.IsAuthenticated]