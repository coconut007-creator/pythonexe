import unittest
from survey import AnonymousSurvey
class TestAnonymous(unittest.TestCase):
    def test_store(self):
        question = "What language did you first learn to speak"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

unittest.main()