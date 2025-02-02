from django.db import models
from django.utils import timezone

class Athlete(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    team = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AthleteAssessmentMetric(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)  # Make sure 'Athlete' is correctly imported
    metric_name = models.CharField(max_length=255)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.athlete} - {self.metric_name}: {self.score}"

class AthleteGoal(models.Model):
    """
    Stores goals set by an athlete for specific sessions.
    """
    athlete_name = models.CharField(max_length=100)
    session_name = models.CharField(max_length=100)
    goal_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.athlete_name} - {self.session_name}"

class ChatbotConversation(models.Model):
    """
    Tracks conversations between a participant and the chatbot.
    """
    participant = models.ForeignKey(
        "Participant", on_delete=models.CASCADE, related_name="conversations"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversation {self.id} with {self.participant.name}"

class ChatbotMessages(models.Model):
    """
    Stores messages exchanged in a chatbot conversation.
    """
    conversation = models.ForeignKey(
        ChatbotConversation, on_delete=models.CASCADE, related_name="messages"
    )
    sender = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.message[:50]}"

class Metric(models.Model):
    """
    Represents a specific metric for assessing participants.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class MetricSession(models.Model):
    """
    Stores session-based metrics for participants, including pre- and post-scores.
    """
    participant_name = models.CharField(max_length=100)
    metric_name = models.CharField(max_length=255)
    pre_score = models.IntegerField()
    post_score = models.IntegerField()
    session = models.IntegerField()

    def __str__(self):
        return f"{self.participant_name} - {self.metric_name} (Session {self.session})"


class Notifications(models.Model):
    """
    Stores notifications for participants.
    """
    participant = models.ForeignKey(
        "Participant", on_delete=models.CASCADE, related_name="notifications"
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.participant.name}"


class Participant(models.Model):
    """
    Represents a participant in a session.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class SportsTeamLeadershipEvaluation(models.Model):
    """
    Stores self-evaluation and peer feedback for sports team leadership.
    """
    athlete_name = models.CharField(max_length=100)
    session_name = models.CharField(max_length=100)
    question_number = models.IntegerField(default=1)
    category = models.CharField(max_length=50, default="Unknown")
    question_text = models.TextField()
    response = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "sports_team_leadership_evaluation"

    def __str__(self):
        return f"{self.athlete_name} - {self.session_name} - {self.question_number}"

class AssessmentMetric(models.Model):
    participant_name = models.CharField(max_length=100)
    session_number = models.IntegerField()
    metric_name = models.CharField(max_length=255)
    pre_score = models.IntegerField()
    post_score = models.IntegerField()

    def __str__(self):
        return f"{self.participant_name} - Session {self.session_number} - {self.metric_name}"

class Feedback(models.Model):
    participant_name = models.CharField(max_length=100)
    session_number = models.IntegerField()
    feedback_text = models.TextField()

    def __str__(self):
        return f"{self.participant_name} - Session {self.session_number}"

class Session1Assessment(models.Model):
    participant_name = models.CharField(max_length=255)
    habit_goal_confidence = models.IntegerField()
    self_performance_confidence = models.IntegerField()
    teammate_performance_confidence = models.IntegerField()
    goal_success_rate = models.IntegerField()
    school_discipline = models.IntegerField()

    def __str__(self):
        return self.participant_name

class Session2Feedback(models.Model):
    participant_name = models.CharField(max_length=255)
    leadership_confidence_pre = models.IntegerField()
    leadership_confidence_post = models.IntegerField()
    accountability_pre = models.IntegerField()
    accountability_post = models.IntegerField()
    responsibility_pre = models.IntegerField()
    responsibility_post = models.IntegerField()
    proactiveness_pre = models.IntegerField()
    proactiveness_post = models.IntegerField()
    team_culture_pre = models.IntegerField()
    team_culture_post = models.IntegerField()

    def __str__(self):
        return self.participant_name

class Session3Feedback(models.Model):
    participant_name = models.CharField(max_length=255)
    responsibility_pre = models.IntegerField()
    responsibility_post = models.IntegerField()
    focus_control_pre = models.IntegerField()
    focus_control_post = models.IntegerField()
    follow_through_pre = models.IntegerField()
    follow_through_post = models.IntegerField()
    team_accountability_pre = models.IntegerField()
    team_accountability_post = models.IntegerField()
    conscious_decision_pre = models.IntegerField()
    conscious_decision_post = models.IntegerField()
    accountability_pre = models.IntegerField()
    accountability_post = models.IntegerField()
    enforcer_pre = models.IntegerField()
    enforcer_post = models.IntegerField()

    def __str__(self):
        return self.participant_name

class Session4Feedback(models.Model):
    participant_name = models.CharField(max_length=255)
    confidence_success_pre = models.IntegerField()
    confidence_success_post = models.IntegerField()
    best_athlete_pre = models.IntegerField()
    best_athlete_post = models.IntegerField()

    def __str__(self):
        return self.participant_name

class Session5Feedback(models.Model):
    participant_name = models.CharField(max_length=255)
    lead_by_example_pre = models.IntegerField()
    lead_by_example_post = models.IntegerField()
    learning_growth_pre = models.IntegerField()
    learning_growth_post = models.IntegerField()
    leadership_confidence_pre = models.IntegerField()
    leadership_confidence_post = models.IntegerField()
    communication_confidence_pre = models.IntegerField()
    communication_confidence_post = models.IntegerField()

    def __str__(self):
        return self.participant_name
