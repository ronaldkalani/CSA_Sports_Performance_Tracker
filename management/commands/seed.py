from core_api.models import Participant, Session, AssessmentMetrics

# Participant Data
participants_data = [
    "Matt", "Braeden", "Cameron", "Mark", "Alexi", "Hudson", "Lucas C", "Lucas M",
    "Devun", "Josh", "Logan", "Mike", "Greg", "Kevin", "Scott", "Taylor",
    "Markus", "Shaun", "Jackson"
]

# Session Data
sessions_data = [
    {"session_number": 1, "description": "Pre and Post Assessment"},
    {"session_number": 2, "description": "Leadership Confidence Assessment"},
    {"session_number": 3, "description": "Responsibility and Accountability Assessment"},
    {"session_number": 4, "description": "Confidence and Success Assessment"},
    {"session_number": 5, "description": "Leadership and Personal Growth Assessment"},
]

# Metrics Data for Each Session
metrics_data = {
    1: {  # Session 1 Metrics
        "confidence_in_habit_building_pre": [7, 8, 8, 5, 8, 6, 7, 7, 8, 7, 6, 8, 8, 5, 7, 9, 6, 6, 6],
        "confidence_in_habit_building_post": [8, 9, 9, 8, 9, 8, 8, 9, 9, 8, 8, 8, 9, 8, 9, 9, 8, 8, 8],
        "consistent_performance_self_pre": [9, 8, 7, 8, 8, 8, 7, 8, 9, 8, 7, 7, 8, 7, 7, 8, 6, 7, 7],
        "consistent_performance_self_post": [9, 9, 9, 8, 9, 8, 9, 9, 9, 9, 9, 8, 9, 8, 8, 9, 9, 8, 8],
        "consistent_performance_teammates_pre": [8, 8, 7, 7, 9, 8, 7, 9, 8, 8, 7, 7, 8, 7, 7, 8, 6, 7, 7],
        "consistent_performance_teammates_post": [9, 9, 8, 8, 9, 8, 8, 9, 8, 9, 9, 8, 9, 8, 8, 9, 9, 8, 8],
        "goal_success_rate_pre": [7, 7, 9, 5, 9, 7, 7, 7, 8, 6, 7, 7, 6, 6, 5, 7, 5, 6, 7],
        "goal_success_rate_post": [9, 9, 9, 8, 9, 8, 8, 9, 8, 9, 8, 9, 8, 8, 8, 9, 8, 8, 9],
        "discipline_in_school_pre": [9, 9, 8, 6, 9, 8, 7, 7, 8, 8, 8, 7, 8, 8, 7, 7, 8, 8, 7],
        "discipline_in_school_post": [9, 9, 8, 8, 9, 8, 8, 8, 8, 9, 8, 7, 8, 8, 7, 8, 8, 8, 7],
    },
    2: {  # Session 2 Metrics
        "leadership_inspiration_pre": [8, 8, 7, 7, 8, 8, 7, 8, 8, 8, 8, 7, 8, 7, 8, 7, 7, 7, 7],
        "leadership_inspiration_post": [8, 9, 8, 8, 9, 8, 8, 8, 9, 9, 8, 8, 9, 7, 8, 8, 8, 8, 8],
        "accountability_team_outcomes_pre": [9, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 7, 8, 7, 8, 7, 8, 7, 7],
        "accountability_team_outcomes_post": [9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 8, 9, 8, 9, 8, 8, 9, 9],
        "responsibility_team_success_pre": [9, 8, 7, 8, 9, 8, 8, 8, 8, 8, 8, 7, 8, 7, 8, 7, 8, 7, 7],
        "responsibility_team_success_post": [9, 9, 9, 8, 9, 9, 9, 8, 9, 9, 9, 8, 9, 8, 9, 8, 8, 9, 9],
        "proactivity_feedback_pre": [7, 8, 9, 6, 9, 7, 8, 8, 9, 7, 8, 7, 8, 7, 8, 7, 8, 7, 7],
        "proactivity_feedback_post": [8, 9, 9, 8, 9, 9, 9, 8, 9, 8, 8, 8, 9, 8, 8, 8, 8, 9, 8],
        "accountability_inclusive_culture_pre": [9, 8, 9, 6, 9, 7, 8, 8, 9, 7, 8, 8, 8, 7, 8, 7, 8, 8, 7],
        "accountability_inclusive_culture_post": [9, 9, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 8, 9, 9],
    },
    3: {  # Session 3 Metrics
        "responsibility_daily_choices_pre": [7, 7, 8, 7, 8, 7, 8, 8, 9, 8, 8, 7, 8, 7, 8, 7, 7, 7, 7],
        "responsibility_daily_choices_post": [9, 9, 9, 8, 9, 9, 9, 9, 9, 8, 9, 8, 9, 8, 9, 9, 8, 8, 9],
        "control_of_factors_pre": [7, 8, 8, 8, 8, 7, 8, 8, 9, 8, 8, 7, 8, 7, 8, 7, 7, 7, 7],
        "control_of_factors_post": [9, 9, 9, 8, 9, 9, 9, 9, 9, 8, 9, 8, 9, 8, 9, 9, 8, 8, 9],
    },
    4: {  # Session 4 Metrics
        "confidence_success_relation_pre": [8, 8, 7, 6, 9, 8, 7, 8, 8, 7, 8, 7, 8, 7, 7, 8, 7, 7, 7],
        "confidence_success_relation_post": [9, 9, 8, 8, 9, 9, 8, 8, 9, 8, 9, 8, 9, 8, 8, 9, 8, 8, 8],
        "athlete_best_self_pre": [9, 8, 7, 7, 9, 8, 8, 8, 9, 8, 8, 7, 8, 7, 7, 8, 8, 7, 7],
        "athlete_best_self_post": [9, 9, 8, 8, 9, 9, 8, 8, 9, 9, 8, 8, 9, 8, 8, 9, 8, 8, 8],
    },
    5: {  # Session 5 Metrics
        "ethical_leadership_pre": [9, 8, 7, 7, 9, 8, 8, 8, 9, 8, 8, 7, 8, 7, 7, 8, 8, 7, 7],
        "ethical_leadership_post": [9, 9, 8, 8, 9, 9, 8, 8, 9, 9, 8, 8, 9, 8, 8, 9, 8, 8, 8],
    },
}

# Create Participants
participants = []
for name in participants_data:
    participant, created = Participant.objects.get_or_create(name=name)
    participants.append(participant)

# Create Sessions and Metrics
for session_data in sessions_data:
    session, created = Session.objects.get_or_create(
        session_number=session_data["session_number"],
        description=session_data["description"],
    )
    for idx, participant in enumerate(participants):
        metrics = metrics_data[session.session_number]
        AssessmentMetrics.objects.create(
            participant=participant,
            session=session,
            **{metric: values[idx] for metric, values in metrics.items()},
        )
