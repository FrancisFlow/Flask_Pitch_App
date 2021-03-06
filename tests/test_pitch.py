import unittest
from app import db
from app.models import Pitch

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch= Pitch(id=400, pitch_category='funny', pitch_upvote=0, pitch_body="This should be enough", posted_by="John Doe")
    def tearDown(self):
        Pitch.query.delete()
        db.session.commit()
    def test_instance(self):
        self.assertEqual(self.new_pitch.pitch_category, 'funny')
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch(self):
        self.new_pitch.save_pitch()
        pitch=Pitch.get_pitch_by_id(400)
        self.assertEqual(pitch.pitch_category, "funny")
    def test_get_pitch_by_category(self):
        self.new_pitch.save_pitch()
        got_pitch=Pitch.get_pitch("funny")
        self.assertEqual(got_pitch.id, 400)

