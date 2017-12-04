import nose

def status(fun):
    def test_new( *args, **kwargs):
        print("\nRunning test: {}".format(fun.__name__))
        fun(*args, **kwargs)
    return test_new

@status
def sanity_test():
    assert True
