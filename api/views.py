# ==========================
# 📌 Standard Library Imports
# ==========================
import json

# ==========================
# 📌 Django Imports
# ==========================
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

# ==========================
# 📌 Local Serializers Import
# ==========================
from core_api.serializers import (
    AthleteSerializer, AthleteAssessmentMetricSerializer, AthleteGoalSerializer, 
    ChatbotConversationSerializer, ChatbotMessagesSerializer, AssessmentMetricSerializer, 
    FeedbackSerializer, MetricSerializer, MetricSessionSerializer, NotificationsSerializer, 
    ParticipantSerializer, SportsTeamLeadershipEvaluationSerializer, Session1AssessmentSerializer, 
    Session2FeedbackSerializer, Session3FeedbackSerializer, Session4FeedbackSerializer, 
    Session5FeedbackSerializer
)

# ==========================
# 📌 BASIC VIEWS (HTML Pages)
# ==========================

def home(request):
    """ Simple home page returning a welcome message. """
    return HttpResponse("Welcome to the CSA Sports Performance Tracker!")


def home_view(request):
    """ Renders the home page with assessment metrics data. """
    from core_api.models import AthleteAssessmentMetric  # ✅ Import inside function
    metrics = AthleteAssessmentMetric.objects.all()
    return render(request, 'home.html', {'metrics': metrics})


def assessment_visualization(request):
    """ Renders an assessment visualization page with sample data. """
    try:
        data = {"message": "Assessment visualization data"}
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def response_list(request):
    """ Renders a template displaying feedback responses. """
    try:
        from core_api.models import Feedback  # ✅ Import inside function
        responses = Feedback.objects.all()
        return render(request, "response_list.html", {"responses": responses})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ==========================
# 📌 API VIEWS (RESTful APIs)
# ==========================

class GetDataView(APIView):
    """ API endpoint to retrieve data. """
    def get(self, request):
        try:
            data = {"message": "Successfully retrieved data"}
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitDataView(APIView):
    """ API endpoint to submit data. """
    def post(self, request):
        try:
            input_data = request.data.get("input")
            if not input_data:
                return Response({"error": "Input data is required"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Data submitted successfully!", "input": input_data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ==========================
# 📌 BASE VIEWSET (Reusable)
# ==========================

class BaseViewSet(viewsets.ModelViewSet):
    """ Base ViewSet to handle errors globally and optimize queries. """
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ==========================
# 📌 MODEL VIEWSETS (For REST API Endpoints)
# ==========================

class AthleteViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import Athlete  # ✅ Import inside function
        return Athlete.objects.all()
    
    serializer_class = AthleteSerializer


class AthleteAssessmentMetricViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import AthleteAssessmentMetric  # ✅ Import inside function
        return AthleteAssessmentMetric.objects.select_related('athlete')

    serializer_class = AthleteAssessmentMetricSerializer


class AthleteGoalViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import AthleteGoal  # ✅ Import inside function
        return AthleteGoal.objects.select_related('athlete')

    serializer_class = AthleteGoalSerializer


class ChatbotConversationViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import ChatbotConversation  # ✅ Import inside function
        return ChatbotConversation.objects.prefetch_related('messages')

    serializer_class = ChatbotConversationSerializer


class ChatbotMessagesViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import ChatbotMessages  # ✅ Import inside function
        return ChatbotMessages.objects.select_related('conversation')

    serializer_class = ChatbotMessagesSerializer


class AssessmentMetricViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import AssessmentMetric  # ✅ Import inside function
        return AssessmentMetric.objects.all()

    serializer_class = AssessmentMetricSerializer


class FeedbackViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import Feedback  # ✅ Import inside function
        return Feedback.objects.select_related('participant')

    serializer_class = FeedbackSerializer


class MetricViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import Metric  # ✅ Import inside function
        return Metric.objects.all()

    serializer_class = MetricSerializer


class MetricSessionViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import MetricSession  # ✅ Import inside function
        return MetricSession.objects.prefetch_related('metrics')

    serializer_class = MetricSessionSerializer


class NotificationsViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import Notifications  # ✅ Import inside function
        return Notifications.objects.all()

    serializer_class = NotificationsSerializer


class ParticipantViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import Participant  # ✅ Import inside function
        return Participant.objects.all()

    serializer_class = ParticipantSerializer


class SportsTeamLeadershipEvaluationViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import SportsTeamLeadershipEvaluation  # ✅ Import inside function
        return SportsTeamLeadershipEvaluation.objects.select_related('participant')

    serializer_class = SportsTeamLeadershipEvaluationSerializer


class Session1AssessmentViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import Session1Assessment  # ✅ Import inside function
        return Session1Assessment.objects.all()

    serializer_class = Session1AssessmentSerializer


class Session2FeedbackViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import Session2Feedback  # ✅ Import inside function
        return Session2Feedback.objects.all()

    serializer_class = Session2FeedbackSerializer


class Session3FeedbackViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import Session3Feedback  # ✅ Import inside function
        return Session3Feedback.objects.all()

    serializer_class = Session3FeedbackSerializer


class Session4FeedbackViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import Session4Feedback  # ✅ Import inside function
        return Session4Feedback.objects.all()

    serializer_class = Session4FeedbackSerializer


class Session5FeedbackViewSet(BaseViewSet):
    def get_queryset(self):
        from core_api.models import Session5Feedback  # ✅ Import inside function
        return Session5Feedback.objects.all()

    serializer_class = Session5FeedbackSerializer


# ==========================
# 📌 TEST API ENDPOINT
# ==========================
def test_api(request):
    from core_api.models import Athlete  # ✅ Import inside the function
    athletes = Athlete.objects.all()
    return JsonResponse({"athletes_count": athletes.count()})
