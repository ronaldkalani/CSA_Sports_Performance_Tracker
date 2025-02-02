from rest_framework import serializers
from .models import (
    Athlete, AthleteAssessmentMetric, AthleteGoal, ChatbotConversation, ChatbotMessages,
    Metric, MetricSession, Notifications, Participant, SportsTeamLeadershipEvaluation,
    AssessmentMetric, Feedback, Session1Assessment, Session2Feedback, Session3Feedback,
    Session4Feedback, Session5Feedback
)

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'  # Serialize all fields

class AthleteAssessmentMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteAssessmentMetric
        fields = '__all__'

class AthleteGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteGoal
        fields = '__all__'

class ChatbotConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatbotConversation
        fields = '__all__'

class ChatbotMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatbotMessages
        fields = '__all__'

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'

class MetricSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricSession
        fields = '__all__'

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class SportsTeamLeadershipEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsTeamLeadershipEvaluation
        fields = '__all__'

class AssessmentMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentMetric
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class Session1AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session1Assessment
        fields = '__all__'

class Session2FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session2Feedback
        fields = '__all__'

class Session3FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session3Feedback
        fields = '__all__'

class Session4FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session4Feedback
        fields = '__all__'

class Session5FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session5Feedback
        fields = '__all__'
