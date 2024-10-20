def caching_fibonacci(n):
    cache = {}
    
    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 0:
            return 0
        if n == 1:
            return 1

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci(n)

print(caching_fibonacci(10))  # 55
print(caching_fibonacci(50))  # 12586269025