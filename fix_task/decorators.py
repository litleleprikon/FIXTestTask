#!/usr/bin/env python
__author__ = 'litleleprikon'


def args_match_types(func):
    """
    Decorator, that checks that types of named arguments is matches to types, allowed in annotations of function
    :param func: function to check
    :return: wrapper, that will check args
    """

    def wrapper(*args, **kwargs):
        for arg_k, arg_v in kwargs.items():
            if arg_v is not None and not isinstance(arg_v, func.__annotations__.get(arg_k, arg_v.__class__)):
                raise TypeError(
                    "Function %s must have argument type of %s is %s",
                    func.__name__,
                    arg_k,
                    func.__annotations__[arg_k]
                )
        return func(*args, **kwargs)
    return wrapper
