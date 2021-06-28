import functools

class DontCache(Exception):
    def __init__(self, data):
        super().__init__("don't cache this result")
        self.data = data

def unwrap_dontcache(fn):
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except DontCache as e:
            return e.data

    return wrapped

def filtered_lru_cache(filter, maxsize=128, typed=False):
    def filtered_lru_cache_decorator(fn):
        @functools.wraps(fn)
        @unwrap_dontcache
        @functools.lru_cache(maxsize=maxsize, typed=typed)
        def wrapped(*args, **kwargs):
            result = fn(*args, **kwargs)
            if not filter(result):
                raise DontCache(result)
            else:
                return result

        return wrapped

    return filtered_lru_cache_decorator
