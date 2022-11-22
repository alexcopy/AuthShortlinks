from celery import Celery

app = Celery('tasks', broker='redis://')


@app.task(name='tasks.add', default_retry_delay=5)
def add(x, y):
    print(x + y)
    return x + y


@app.task(name='tasks.fib', default_retry_delay=5)
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + n
