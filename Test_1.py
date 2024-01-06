def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            last_res = cache.setdefault(n, fibonacci(n-1) + fibonacci(n-2))
            return last_res

    return fibonacci