import json
import mock
import nose
import unittest

from nose.tools import assert_equal


def status(fun):
    def test_new( *args, **kwargs):
        class_name = str(fun).split('.')[0].split(' ')[1]
        print(
            "\nRunning test: {}.{}... ".format(class_name, fun.__name__),
            end=""
        ) 
        fun(*args, **kwargs)
        print("\033[92m✓\x1b[0m")
    return test_new

@status
def sanity_test():
    assert True


class SlotsCommandTests(unittest.TestCase):
    def setUp(self):
        from commands.slots import gen_slot_results, check_win
        self.gen_slot_results = gen_slot_results
        self.check_win = check_win

    @status
    def test_results_trivial(self):
        results = self.gen_slot_results(
            ['1'],
            3
        )

        assert results == ['1', '1', '1']

    @status
    def test_check_win_positive_trivial(self):
        assert self.check_win([1, 1, 1])

    @status
    def test_check_win_negative_trivial(self):
        assert self.check_win([1, 2, 3]) == False

    @status
    def test_check_win_nonlist(self):
        assert self.check_win(10) == False

    @status
    def test_check_win_string(self):
        assert self.check_win('111') == False

    @status
    def test_check_win_empty(self):
        assert self.check_win([]) == False

class DiceCommandTests(unittest.TestCase):
    def setUp(self):
        from commands.dice import get_value
        self.get_value = get_value

    @status
    def test_positive(self):
        import random
        for _ in range(100):
            max = random.randint(1, 20)
            value = self.get_value(max)
            assert value <= max
            assert value > 0

    @status
    def test_negative(self):
        value = self.get_value(-20)
        assert value is False

    @status
    def test_zero(self):
        value = self.get_value(0)
        assert value is False

    @status
    def test_float(self):
        value = self.get_value(19.2)
        assert value <= 19
        assert value > 0

    @status
    def test_non_number(self):
        value = self.get_value('squirrel')
        assert value is False

    @status
    def test_parsing(self):
        import random
        for _ in range(100):
            max = str(random.randint(1, 20))
            value = self.get_value(max)
            assert value <= int(max)
            assert value > 0
        
    @status
    def test_list(self):
        value = self.get_value([])
        assert value is False

    @status
    def test_dict(self):
        value = self.get_value({})
        assert value is False

    @status
    def test_object(self):

        class DiceTest:
            pass
        
        value = self.get_value(DiceTest())
        assert value is False


class VersionCommandTests(unittest.TestCase):
    def setUp(self):
        from commands.version import get_version_hash
        self.get_version_hash = get_version_hash

    @status
    def test_get_version_hash(self):
        subprocess = mock.Mock()
        subprocess.check_output = mock.Mock(return_value=b'test output')
        output = self.get_version_hash(subprocess)

        assert subprocess.check_output.called
        assert subprocess.check_output.call_count == 1
        assert output == 'test output'
        
    

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
