import json
import mock
import nose
import unittest

from nose.tools import assert_equal


def status(fun):
    def test_new( *args, **kwargs):
        print("\nRunning test: {}... ".format(fun.__name__), end="")
        fun(*args, **kwargs)
        print("\033[92m✓\x1b[0m")
    return test_new

@status
def sanity_test():
    assert True


class MovieCommandTests(unittest.TestCase):

    def setUp(self):
        from commands.movie import get_movie_info
        self.movie_command = get_movie_info

    @status
    def test_get_info(self):
        query = 'test'
        requests = mock.Mock()
        def fake_get(query):
            response = mock.Mock()
            response.text = json.dumps({
                'Title': 'test title',
                'Year': 'test year',
                'Runtime': 'test runtime',
                'Genre': 'test genre',
                'Country': 'test country',
                'Plot': 'test plot',
                'Poster': 'test poster url'
            })
            
            return response
        requests.get = fake_get
        
        output = self.movie_command(query, requests)
        assert_equal(output[0], 'Title: test title\nYear: test year\nRuntime: test runtime\nGenre: test genre\nCountry: test country\nPlot: test plot')
        assert_equal(output[1], 'test poster url')
        


    @status
    def test_get_info_error(self):
        query = 'test'
        requests = mock.Mock()
        def fake_get(query):
            response = mock.Mock()
            response.text = json.dumps({
                'Error': 'test error'
            })
            return response
        requests.get = fake_get

        output = self.movie_command(query, requests)
        assert_equal(len(output), 1)
        assert_equal(output[0], 'test error')
