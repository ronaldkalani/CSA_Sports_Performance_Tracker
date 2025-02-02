from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Import views from the same app

# Create a router for API endpoints
router = DefaultRouter()

# ✅ Register ViewSets with explicit basenames
router.register(r'assessment-metrics', views.AssessmentMetricViewSet, basename='assessment-metric')
router.register(r'athlete-goals', views.AthleteGoalViewSet, basename='athlete-goal')
router.register(r'chatbot-conversations', views.ChatbotConversationViewSet, basename='chatbot-conversation')
router.register(r'feedbacks', views.FeedbackViewSet, basename='feedback')
router.register(r'metric-sessions', views.MetricSessionViewSet, basename='metric-session')
router.register(r'metrics', views.MetricViewSet, basename='metric')
router.register(r'notifications', views.NotificationsViewSet, basename='notifications')  # Fixed name
router.register(r'participants', views.ParticipantViewSet, basename='participant')

urlpatterns = [
    path('', include(router.urls)),  # Include DRF router URLs
]
