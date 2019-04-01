import functools
import warnings


def deprecated(deadline_date, msg=''):
    def deprecated_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                '{} {} is deprecated API and will be removed on {}. {}'.format(
                    args[0].__class__.__name__, func.__name__,
                    deadline_date, msg).strip(),
                FutureWarning
            )
            return func(*args, **kwargs)
        return wrapper
    return deprecated_decorator
