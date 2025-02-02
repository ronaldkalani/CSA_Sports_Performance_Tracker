# ==========================
# 📌 Standard Library Imports
# ==========================
import json
import logging

# ==========================
# 📌 Django Imports
# ==========================
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

# ==========================
# 📌 DRF Imports
# ==========================
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

# ==========================
# 📌 Local Serializers & Models Import
# ==========================
from core_api.serializers import (
    AthleteSerializer, FeedbackSerializer, AthleteAssessmentMetricSerializer
)
from core_api.models import Athlete, Feedback, AthleteAssessmentMetric

# ==========================
# 📌 Logger Configuration
# ==========================
logger = logging.getLogger(__name__)


# ==========================
# 📌 BASIC HTML VIEWS
# ==========================

def home_view(request):
    """ Renders the home page with assessment metrics data. """
    metrics = AthleteAssessmentMetric.objects.all()
    return render(request, 'home.html', {'metrics': metrics})


def assessment_visualization(request):
    """ Renders an assessment visualization page with sample data. """
    try:
        data = {"message": "Assessment visualization data"}
        return JsonResponse(data)
    except Exception as e:
        logger.error(f"Error in assessment_visualization: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500)


def response_list(request):
    """ Renders a template displaying feedback responses. """
    try:
        responses = Feedback.objects.all()
        return render(request, "response_list.html", {"responses": responses})
    except Exception as e:
        logger.error(f"Error fetching feedback responses: {str(e)}")
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
            logger.error(f"Error in GetDataView: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitDataView(APIView):
    """ API endpoint to submit data. """
    def post(self, request):
        try:
            input_data = request.data.get("input")
            if not input_data:
                return Response(
                    {"error": "Input data is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {"message": "Data submitted successfully!", "input": input_data},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            logger.error(f"Error in SubmitDataView: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ==========================
# 📌 BASE VIEWSET (Reusable)
# ==========================

class BaseViewSet(viewsets.ModelViewSet):
    """ Base ViewSet to handle errors globally and optimize queries. """
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error in BaseViewSet: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ==========================
# 📌 MODEL VIEWSETS (For REST API Endpoints)
# ==========================

class AthleteViewSet(BaseViewSet):
    """ ViewSet for managing Athletes """
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class AthleteAssessmentMetricViewSet(BaseViewSet):
    """ ViewSet for Athlete Assessment Metrics """
    queryset = AthleteAssessmentMetric.objects.select_related('athlete')
    serializer_class = AthleteAssessmentMetricSerializer


class FeedbackViewSet(BaseViewSet):
    """ ViewSet for Feedback data """
    queryset = Feedback.objects.select_related('participant')
    serializer_class = FeedbackSerializer


# ==========================
# 📌 TEST API ENDPOINT
# ==========================

def test_api(request):
    """ Test API to check Athlete count. """
    athletes_count = Athlete.objects.count()
    return JsonResponse({"athletes_count": athletes_count})
