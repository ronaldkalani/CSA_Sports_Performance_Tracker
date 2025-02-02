from django.urls import path, re_path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import (
    GetDataView, SubmitDataView, AthleteViewSet, AthleteAssessmentMetricViewSet, 
    AthleteGoalViewSet, ChatbotConversationViewSet, ChatbotMessagesViewSet, 
    MetricViewSet, MetricSessionViewSet, NotificationsViewSet, ParticipantViewSet, 
    SportsTeamLeadershipEvaluationViewSet, AssessmentMetricViewSet, FeedbackViewSet, 
    Session1AssessmentViewSet, Session2FeedbackViewSet, Session3FeedbackViewSet, 
    Session4FeedbackViewSet, Session5FeedbackViewSet
)

# ==========================
# 📌 API Router Setup
# ==========================
router = DefaultRouter()
router.register(r'athletes', AthleteViewSet)
router.register(r'athlete-assessment-metrics', AthleteAssessmentMetricViewSet)
router.register(r'athlete-goals', AthleteGoalViewSet)
router.register(r'chatbot-conversations', ChatbotConversationViewSet)
router.register(r'chatbot-messages', ChatbotMessagesViewSet)
router.register(r'metrics', MetricViewSet)
router.register(r'metric-sessions', MetricSessionViewSet)
router.register(r'notifications', NotificationsViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'sports-leadership-evaluations', SportsTeamLeadershipEvaluationViewSet)
router.register(r'assessment-metrics', AssessmentMetricViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'session1-assessment', Session1AssessmentViewSet)
router.register(r'session2-feedback', Session2FeedbackViewSet)
router.register(r'session3-feedback', Session3FeedbackViewSet)
router.register(r'session4-feedback', Session4FeedbackViewSet)
router.register(r'session5-feedback', Session5FeedbackViewSet)

# ==========================
# 📌 URL Patterns
# ==========================
urlpatterns = [
    # ✅ REST API Endpoints
    path('api/', include(router.urls)),  
    path('api/assessment-visualization/', GetDataView.as_view(), name="assessment_visualization"),
    path('api/submit-data/', SubmitDataView.as_view(), name="submit_data"),

    # ✅ Catch-all pattern for React frontend
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
