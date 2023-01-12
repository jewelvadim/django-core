from functools import wraps
from time import perf_counter
from typing import Any, Callable, Unpack

from django.db import connection, reset_queries


def query_debugger(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args: Unpack, **kwargs: Unpack) -> Any:
        reset_queries()

        start_queries = len(connection.queries)

        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()

        end_queries = len(connection.queries)

        print(f'Function : {func.__name__}')
        print(f'Number of Queries : {end_queries - start_queries}')
        print(f'Finished in : {(end - start):.2f}s')

        return result

    return wrapper
