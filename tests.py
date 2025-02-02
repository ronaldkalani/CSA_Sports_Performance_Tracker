from django.test import TestCase
from core_api.models import Participant, Session, AssessmentMetrics

class CoreAPITestCase(TestCase):
    def setUp(self):
        self.participant = Participant.objects.create(name="Test User", email="test.user@example.com", age=30, team="Team X")
        self.session = Session.objects.create(session_number=1, description="Test Session")

    def test_create_assessment_metrics(self):
        metrics = AssessmentMetrics.objects.create(
            participant=self.participant,
            session=self.session,
            confidence_in_habit_building_pre=5,
            confidence_in_habit_building_post=8,
            consistent_performance_self_pre=7,
            consistent_performance_self_post=9,
            # Add values for other fields
        )
        self.assertEqual(metrics.participant.name, "Test User")
        self.assertEqual(metrics.session.description, "Test Session")

