class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    raise MyException("Wystąpił wyjątek")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\or-19-06\kl11.py", line 6, in <module>
#     raise MyException("Wystąpił wyjątek")
# MyException: Wystąpił wyjątek
except MyException:
    print("Wystąpił wyjątek MyException")
