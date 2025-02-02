
from django.contrib import admin
from .models import (
    AssessmentMetric,
    AthleteGoal,
    ChatbotConversation,
    ChatbotMessages,
    Feedback,
    Metric,
    MetricSession,
    Notifications,
    Participant,
    SportsTeamLeadershipEvaluation,
)

@admin.register(AssessmentMetric)
class AssessmentMetricAdmin(admin.ModelAdmin):
    list_display = ('participant_name', 'session_number', 'metric_name', 'pre_score', 'post_score')
    search_fields = ('participant_name', 'metric_name')

@admin.register(AthleteGoal)
class AthleteGoalAdmin(admin.ModelAdmin):
    list_display = ("athlete_name", "session_name", "goal_description", "start_date", "end_date", "completed", "created_at")
    list_filter = ("session_name", "completed")
    search_fields = ("athlete_name", "session_name")
    ordering = ("-created_at",)

@admin.register(ChatbotConversation)
class ChatbotConversationAdmin(admin.ModelAdmin):
    list_display = ("participant", "created_at", "updated_at")
    search_fields = ("participant__name",)
    ordering = ("-created_at",)

@admin.register(ChatbotMessages)
class ChatbotMessagesAdmin(admin.ModelAdmin):
    list_display = ("conversation", "sender", "message", "timestamp")
    search_fields = ("conversation__participant__name", "sender")
    ordering = ("-timestamp",)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('participant_name', 'session_number', 'feedback_text')
    search_fields = ('participant_name', 'session_number')

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

@admin.register(MetricSession)
class MetricSessionAdmin(admin.ModelAdmin):
    list_display = ("participant_name", "metric_name", "pre_score", "post_score", "session")
    search_fields = ("participant_name", "metric_name")
    ordering = ("session",)

@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ("participant", "message", "is_read", "created_at")
    list_filter = ("is_read",)
    search_fields = ("participant__name", "message")
    ordering = ("-created_at",)

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")
    ordering = ("name",)

@admin.register(SportsTeamLeadershipEvaluation)
class SportsTeamLeadershipEvaluationAdmin(admin.ModelAdmin):
    list_display = ("athlete_name", "session_name", "question_number", "category", "question_text", "response", "created_at")
    list_filter = ("session_name", "category")
    search_fields = ("athlete_name", "session_name", "question_text")
    ordering = ("-created_at",)

from django.contrib import admin
from .models import Session1Assessment, Session2Feedback, Session3Feedback, Session4Feedback, Session5Feedback

admin.site.register(Session1Assessment)
admin.site.register(Session2Feedback)
admin.site.register(Session3Feedback)
admin.site.register(Session4Feedback)
admin.site.register(Session5Feedback)

