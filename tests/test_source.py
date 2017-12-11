import unittest
from app.models import Sources


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(
            'abc-news-au', 'ABC NEWS', 'The best news in Australia', 'https://abcnews.au', 'general', 'en', 'au')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))
