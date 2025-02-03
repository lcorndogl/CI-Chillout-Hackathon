from django.test import TestCase
from django.contrib.auth.models import User
from .models import Score

class ScoreModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.score = Score.objects.create(user=self.user, score=123.45)

    def test_score_creation(self):
        self.assertEqual(self.score.user.username, 'testuser')
        self.assertEqual(self.score.score, 123.45)
        self.assertFalse(self.score.hidden)

    def test_score_hidden_default(self):
        self.assertFalse(self.score.hidden)

    def test_score_set_hidden(self):
        self.score.hidden = True
        self.score.save()
        self.assertTrue(self.score.hidden)

    def test_score_set_visible(self):
        self.score.hidden = True
        self.score.save()
        self.score.hidden = False
        self.score.save()
        self.assertFalse(self.score.hidden)

    def test_score_deletion(self):
        score_id = self.score.id
        self.score.delete()
        with self.assertRaises(Score.DoesNotExist):
            Score.objects.get(id=score_id)
