import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czad wykonania funkcji {func.__name__}: {execution_time} sec")
        return result

    return wrapper


@measure_time
def my_function():
    # pass
    time.sleep(2)  # wstrzymanie działąnia programu na 2 sekundy


my_function()  # Czad wykonania funkcji my_function: 2.0007550716400146 sec
