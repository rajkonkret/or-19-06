def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    return f"Hello {name}"


greetings = greet("Radek")
for g in greetings:
    print(g)
