def logging(func):
    """Log when a function is called."""
    def log_call(*args, **kwargs):
        print('calling function {}'.format(func.__name__))
        return func(*args, **kwargs)
    return log_call

@logging
def test_function():
    print("hello world")

for i in range(3):
    test_function()